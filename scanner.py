import socket
import subprocess
import platform
import argparse

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
# Escaneo de un puerto
# -----------------------------
def scan_port(host, port, timeout=1):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

# -----------------------------
# Escaneo de varios puertos
# -----------------------------
def port_scan(host, ports, timeout=1):
    abiertos = []
    for port in ports:
        if scan_port(host, port, timeout):
            abiertos.append(port)
    return abiertos

# -----------------------------
# Programa principal con argparse
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Escáner de red estilo Nmap")
    parser.add_argument("--network", help="Subred para ping sweep (ej: 192.168.1)")
    parser.add_argument("--host", help="Host para escaneo de puertos")
    parser.add_argument("--ports", help="Rango de puertos (ej: 20-80)")
    args = parser.parse_args()

    if args.network:
        print(f"Escaneando subred {args.network}.0/24...")
        activos = ping_sweep(args.network)
        print("Hosts activos encontrados:")
        for ip in activos:
            print(f" - {ip}")

    if args.host and args.ports:
        start, end = map(int, args.ports.split("-"))
        puertos = range(start, end+1)
        print(f"Escaneando puertos en {args.host}...")
        abiertos = port_scan(args.host, puertos)
        if abiertos:
            print("Puertos abiertos:")
            for p in abiertos:
                print(f" - {p}")
        else:
            print("No se encontraron puertos abiertos.")

if __name__ == "__main__":
    main()
