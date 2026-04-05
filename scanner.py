import socket

def scan_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        print(f"Puerto {port} abierto en {host}")
        s.close()
    except:
        pass

if __name__ == "__main__":
    host = "127.0.0.1"  # dirección local
    for port in range(20, 1025):
        scan_port(host, port)
