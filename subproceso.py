# Crear un script para saber el nombre de la red y 
# del usuario de la pc donde se está ejecutando
# dicho script.

import subprocess

print("Ejecutando subproceso...")

p = subprocess.run("whoami", capture_output=True, encoding='cp850')

print("Resultado del proceso:", p.returncode)

salida = p.stdout.strip()

nombre_red, nombre_usuario = salida.split("\\")

print("Tu nombre de red es:", nombre_red)
print("Tu nombre de usuaro es:", nombre_usuario)

print("Subproceso ejecutado.")