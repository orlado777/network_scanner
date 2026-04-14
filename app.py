from flask import Flask, render_template_string, request
import webbrowser
import threading
import socket

from scanner import port_scan, banner_grab, SERVICIOS_CONOCIDOS, ping, ping_sweep

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Scanner Network</title>
    <style>
        body {
            background: #0d1117;
            color: #00ff9c;
            font-family: Consolas, monospace;
            text-align: center;
        }
        h1 {
            color: #00ff9c;
        }
        .container {
            border: 1px solid #00ff9c;
            padding: 20px;
            margin: 20px auto;
            width: 60%;
            border-radius: 10px;
            box-shadow: 0 0 20px #00ff9c;
        }
        input, select {
            margin: 5px;
            padding: 8px;
            background: black;
            color: #00ff9c;
            border: 1px solid #00ff9c;
        }
        button {
            padding: 10px;
            background: #00ff9c;
            border: none;
            color: black;
            cursor: pointer;
        }
        pre {
            text-align: left;
            background: black;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .title {
            font-size: 28px;
        }
    </style>
</head>

<body>

<h1 class="title">⚡ Scanner_Network ⚡</h1>
<h3>Aponce - Rrojas - OAraya</h3>

<div class="container">
    <form method="post">
        <input type="text" name="host" placeholder="Host (ej: 127.0.0.1)">
        <input type="text" name="ports" placeholder="Puertos (ej: 20-80 o 80)">
        <input type="text" name="network" placeholder="Red (ej: 192.168.1)">
        
        <br><br>

        <select name="scan_type">
            <option value="tcp">TCP Scan</option>
            <option value="syn">SYN Scan</option>
        </select>

        <br><br>

        <button name="action" value="scan">Escanear Puertos</button>
        <button name="action" value="ping">Ping</button>
        <button name="action" value="sweep">Scan Red</button>
    </form>

    <pre>{{ resultado }}</pre>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""

    if request.method == "POST":
        try:
            action = request.form.get("action")
            host = request.form.get("host", "").strip()
            ports = request.form.get("ports", "").strip()
            network = request.form.get("network", "").strip()
            scan_type = request.form.get("scan_type")

            # 🔍 Validar host
            if host:
                try:
                    socket.gethostbyname(host)
                except:
                    return render_template_string(HTML, resultado="❌ Host inválido")

            # 🔘 PING
            if action == "ping":
                if not host:
                    return render_template_string(HTML, resultado="❌ Ingresa un host")
                if ping(host):
                    resultado = f"✔ {host} está ACTIVO"
                else:
                    resultado = f"✖ {host} está INACTIVO"

            # 🌍 SCAN RED
            elif action == "sweep":
                if not network:
                    return render_template_string(HTML, resultado="❌ Ingresa red (ej: 192.168.1)")
                activos = ping_sweep(network)
                resultado = "Hosts activos:\n" + "\n".join(activos)

            # 🔥 ESCANEO DE PUERTOS
            elif action == "scan":
                if not host or not ports:
                    return render_template_string(HTML, resultado="❌ Host y puertos requeridos")

                if "-" in ports:
                    start, end = map(int, ports.split("-"))
                    if end - start > 1000:
                        return render_template_string(HTML, resultado="❌ Máx 1000 puertos")
                    puertos = range(start, end + 1)
                else:
                    puertos = [int(ports)]

                abiertos = port_scan(host, puertos, scan_type=scan_type)

                resultado += f"{'Puerto':<8}{'Estado':<10}{'Servicio':<12}\n"

                for p in puertos:
                    servicio = SERVICIOS_CONOCIDOS.get(p, "Desconocido")
                    if p in abiertos:
                        try:
                            banner = banner_grab(host, p)
                        except:
                            banner = ""
                        resultado += f"{p:<8}OPEN     {servicio:<12}{banner}\n"
                    else:
                        resultado += f"{p:<8}CLOSED   {servicio}\n"

        except Exception as e:
            resultado = f"Error controlado: {str(e)}"

    return render_template_string(HTML, resultado=resultado)


def open_browser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)