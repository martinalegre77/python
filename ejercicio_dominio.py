# Guardar en una variable la ip del dominio solicitado
# por el usuario e imprimirla

from gettext import find
import subprocess

dominio = input('Ingrese un dominio: ')
p = subprocess.run(['ping', dominio], capture_output=True, encoding='cp850')
salida = p.stdout.strip()

ip = salida[salida.find('[')+1:salida.find(']')]

print('La IP de', dominio, 'es:', ip)