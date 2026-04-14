Network Scanner
Asignatura

Redes Avanzadas - INACAP

<<<<<<< HEAD
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
 
=======
Descripción

Este proyecto consiste en el desarrollo de un escáner de red en Python, inspirado en herramientas como Nmap.

La aplicación permite identificar hosts activos en una subred, detectar puertos abiertos en un host específico y realizar una identificación básica de servicios mediante técnicas de banner grabbing. Además, incorpora una interfaz web para facilitar su uso.

Objetivos
Detectar hosts activos mediante ping sweep
Escanear puertos en un host específico
Identificar servicios mediante banner grabbing
Implementar distintos tipos de escaneo (TCP y SYN)
Integrar una interfaz web para mejorar la interacción
Aplicar control de versiones utilizando Git y GitHub
Documentar el proyecto con ejemplos y capturas
Estructura del Proyecto
/network_scanner
├── scanner.py        # Lógica del escáner
├── app.py            # Interfaz web con Flask
├── requirements.txt  # Dependencias
├── README.md         # Documentación
├── /tests            # Pruebas
├── /images           # Capturas del sistema
Requisitos
Python 3.8 o superior
Sistema operativo: Windows o Linux
Librerías estándar: socket, subprocess, argparse

Instalación de dependencias:

pip install -r requirements.txt
Uso del Script (Modo Consola)
Ping Sweep
python scanner.py --network 192.168.1
Escaneo de Puertos
python scanner.py --host 127.0.0.1 --ports 20-1024
Ayuda
python scanner.py --help
Uso de la Aplicación Web

Ejecutar el siguiente comando:

python app.py

Al ejecutar la aplicación, se abrirá automáticamente una interfaz web en el navegador.

Funcionalidades de la Aplicación
Escaneo de puertos mediante TCP y SYN
Verificación de disponibilidad de un host (ping)
Escaneo de red completa mediante ping sweep
Detección de servicios mediante banner grabbing
Interfaz web para interacción con el usuario
Campos de la Interfaz
Campo	Descripción
Host	Dirección IP o dominio a escanear
Puertos	Rango o puerto específico (ejemplo: 20-80 o 80)
Red	Subred a escanear (ejemplo: 192.168.1)
Capturas
Interfaz Web

Escaneo de Puertos

Estructura del Proyecto

Entorno de Desarrollo

Configuración de Git

Ping Sweep

Escaneo de Puertos (Consola)

Estado del Proyecto
Fase 1: Organización del equipo y repositorio (completada)
Fase 2: Diseño del escáner (completada)
Fase 3: Implementación básica (completada)
Fase 4: Mejoras y funcionalidades adicionales (completada)
Fase 5: Pruebas y documentación (en desarrollo)
Integrantes del Equipo
Líder del proyecto: Orlando Araya
Desarrollador principal: Alexis Ponce
Documentador: Rogger Rojas
Notas Técnicas
Se utiliza la librería socket para el escaneo de puertos TCP
scapy permite implementar escaneo SYN
Flask proporciona la interfaz web
argparse permite la ejecución por línea de comandos
Escaneo UDP

El escaneo UDP no fue implementado debido a su mayor complejidad. A diferencia de TCP, UDP no establece conexión, por lo que se requiere el análisis de respuestas ICMP para determinar el estado de los puertos. Esta funcionalidad queda propuesta como mejora futura.

Mejoras Futuras
Implementación de multithreading para mejorar el rendimiento
Exportación de resultados a archivos
Implementación de escaneo UDP
Detección de sistema operativo remoto
Comparación con herramientas como Nmap
Conclusión

El proyecto cumple con los objetivos planteados, integrando funcionalidades de escaneo de red junto con una interfaz web que facilita su uso. Se logra una herramienta funcional que permite comprender el funcionamiento básico de los escáneres de red utilizados en entornos profesionales.
>>>>>>> fe6f150 (Entrega final proyecto Network Scanner: interfaz web, mejoras y documentación completa)
