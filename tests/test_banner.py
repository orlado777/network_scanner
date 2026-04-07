def banner_grab(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((host, port))
            # Si es HTTP, enviamos una petición básica
            if port == 80:
                request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
                s.sendall(request.encode())
            return s.recv(1024).decode(errors="ignore")
    except Exception:
        return ""
