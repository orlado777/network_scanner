# Network Scanner

## Asignatura
Redes Avanzadas - INACAP

## Descripción
Este proyecto implementa un escáner de red en Python para:
- Identificar hosts activos en una subred usando ping sweep.
- Escanear puertos TCP en un host específico.
- Realizar banner grabbing para detectar servicios básicos.

El script pretende ser una versión sencilla de una herramienta tipo Nmap, con opciones para escaneo TCP connect y SYN.

## Objetivos
- Detectar hosts activos mediante ping sweep.
- Escanear puertos en un host objetivo.
- Identificar servicios conocidos con banner grabbing.
- Documentar el proyecto y presentar resultados en equipo.

## Estructura del Proyecto
- `scanner.py` – Código principal.
- `requirements.txt` – Dependencias del proyecto.
- `README.md` – Documentación.
- `tests/` – Pruebas unitarias.
- `Imagenes/` – Capturas de ejecución.

## Requisitos
- Python 3.8 o superior.
- Windows o Linux.
- Conexión a la red de destino.
- Permisos suficientes para realizar escaneos de red.

### Dependencias
Instala las dependencias con:

```bash
pip install -r requirements.txt
```

> Nota: El escaneo `syn` requiere `scapy`, que debe estar disponible en el entorno Python.

## Uso del Script

### Ayuda

```bash
python scanner.py --help
```

### Ping Sweep (hosts activos)

Escanea la subred completa `X.Y.Z.0/24` a partir de una dirección de red parcial.

```bash
python scanner.py --network 10.190.147
```

### Escaneo de puertos TCP

Escanea un rango de puertos en un host específico.

```bash
python scanner.py --host 127.0.0.1 --ports 20-1024
```

### Escaneo SYN

Para usar SYN scan, añade `--type syn`. En Windows puede ser necesario ejecutar con privilegios de administrador.

```bash
python scanner.py --host 127.0.0.1 --ports 20-1024 --type syn
```

### Guardar resultados

El parámetro `--output` escribe los resultados en un archivo de texto.

```bash
python scanner.py --host 127.0.0.1 --ports 20-1024 --output resultados.txt
```

## Comportamiento del Script

- `--network` busca hosts activos en `network.1` a `network.254`.
- `--host` y `--ports` realizan un escaneo de puertos usando TCP connect por defecto.
- `--type syn` utiliza un SYN scan con Scapy.
- `banner grabbing` intenta leer el banner del servicio en puertos abiertos.

## Servicios conocidos
El script contiene un diccionario de servicios básicos para puertos comunes:
- 21: FTP
- 22: SSH
- 25: SMTP
- 80: HTTP
- 110: POP3
- 143: IMAP
- 443: HTTPS

## Ejemplos de ejecución

- `python scanner.py --network 192.168.1`
- `python scanner.py --host 192.168.1.10 --ports 20-100`
- `python scanner.py --host 192.168.1.10 --ports 20-100 --type syn --output scan.txt`

## Estado del Proyecto
- Fase 1: Organización del equipo y repositorio (completada).
- Fase 2: Diseño del escáner (completada).
- Fase 3: Implementación básica (completada: ping sweep, port scan, argparse, banner grabbing).
- Fase 4: Mejoras (pendiente: multithreading, guardar resultados, GUI con Tkinter).
- Fase 5: Pruebas y documentación con capturas (pendiente).

## Integrantes del Equipo
- **Líder del proyecto:** Orlando Araya
- **Desarrollador principal:** Alexis Ponce
- **Documentador:** Rogger Rojas

## Notas
- Se recomienda ejecutar el escaneo con privilegios adecuados, especialmente para `syn` scan.
- El script usa la librería `socket` y `subprocess` de Python, además de `scapy` para SYN scan.
- Verifica las políticas de red antes de escanear para evitar problemas de seguridad o cumplimiento.
 