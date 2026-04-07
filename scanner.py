import socket
import subprocess
import platform
import argparse
from scapy.all import IP, TCP, sr1   # Para SYN scan

# -----------------------------
# Diccionario de servicios conocidos
# -----------------------------
SERVICIOS_CONOCIDOS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

# -----------------------------
# Función de ping a un host
# -----------------------------
def ping(host, timeout=1):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

# -----------------------------
# Ping sweep en una subred
# -----------------------------
def ping_sweep(network, timeout=1):
    activos = []
    for i in range(1, 255):
        ip = f"{network}.{i}"
        if ping(ip, timeout):
            activos.append(ip)
    return activos

# -----------------------------
# Escaneo de un puerto (TCP Connect)
# -----------------------------
def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False

# -----------------------------
# Escaneo SYN con Scapy
# -----------------------------
def syn_scan(host, port):
    pkt = IP(dst=host)/TCP(dport=port, flags="S")
    resp = sr1(pkt, timeout=1, verbose=0)
    if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:
        return True
    return False

# -----------------------------
# Escaneo de varios puertos
# -----------------------------
def port_scan(host, ports, timeout=1, scan_type="tcp"):
    abiertos = []
    for port in ports:
        if scan_type == "tcp":
            if scan_port(host, port, timeout):
                abiertos.append(port)
        elif scan_type == "syn":
            if syn_scan(host, port):
                abiertos.append(port)
    return abiertos

# -----------------------------
# Banner grabbing (detección de servicios)
# -----------------------------
def banner_grab(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            return s.recv(1024).decode(errors="ignore").strip()
    except Exception:
        return ""

# -----------------------------
# Argumentos técnicos con argparse
# -----------------------------
def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Network Scanner estilo Nmap")
    parser.add_argument("-n", "--network", help="Subred para ping sweep (ej: 192.168.1)")
    parser.add_argument("-H", "--host", help="Host para escaneo de puertos")
    parser.add_argument("-p", "--ports", help="Rango de puertos (ej: 20-80)")
    parser.add_argument("-t", "--type", choices=["tcp", "syn"], default="tcp",
                        help="Tipo de escaneo: tcp (connect) o syn")
    parser.add_argument("-o", "--output", help="Archivo para guardar resultados")
    return parser.parse_args(args)

# -----------------------------
# Programa principal
# -----------------------------
def main():
    args = parse_args()
    resultados = []

    if args.network:
        print(f"Escaneando subred {args.network}.0/24...")
        activos = ping_sweep(args.network)
        print("Hosts activos encontrados:")
        for ip in activos:
            print(f" - {ip}")
            resultados.append(f"Host activo: {ip}")

    if args.host and args.ports:
        start, end = map(int, args.ports.split("-"))
        puertos = range(start, end+1)
        print(f"Escaneando puertos en {args.host} ({args.type})...")
        abiertos = port_scan(args.host, puertos, scan_type=args.type)

        print(f"{'Puerto':<8}{'Estado':<10}{'Servicio':<12}{'Banner'}")
        for p in puertos:
            servicio = SERVICIOS_CONOCIDOS.get(p, "Desconocido")
            if p in abiertos:
                banner = banner_grab(args.host, p)
                print(f"\033[92m{p:<8}{'OPEN':<10}{servicio:<12}{banner}\033[0m")
                resultados.append(f"Puerto {p} abierto - {servicio} - {banner}")
            else:
                print(f"\033[91m{p:<8}{'CLOSED':<10}{servicio:<12}{''}\033[0m")
                resultados.append(f"Puerto {p} cerrado - {servicio}")

    if args.output:
        with open(args.output, "w") as f:
            f.write("\n".join(resultados))
        print(f"Resultados guardados en {args.output}")

if __name__ == "__main__":
    main()
