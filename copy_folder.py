# Crear un programa que copie los archivos de una carpeta a otra carpeta. 
# En lugar de copiar todos los archivos, solo debe copiar aquellos que tengan 
# la extensión indicada por el usuario (por ejemplo, .txt, .pdf, .png, etc.). 

# Tips para resolverlo:

# Chequeen que las carpetas de origen y destino existan. 
# Usen un bucle for para copiar cada uno de los archivos de la carpeta de origen a la carpeta destino. 
# Para copiar solo los archivos con la extensión ingresada por el usuario (p. ej. .pdf), usen condicionales.
# Lean y escriban los archivos en modo "rb" y "wb", respectivamente, para soportar cualquier tipo de archivo.

from operator import concat
import os

origen = input('Ingrese la carpeta de origen: ')
if not os.path.isdir(origen):
    print('La carpeta de origen no existe')
    exit()

destino = input('Ingrese la carpeta de destino: ')
if not os.path.isdir(destino):
    print('La carpeta de destino no existe')
    exit()

extencion = input('Ingrese la extensión: ')

archivos = []

for dir in os.listdir(origen):
    if dir[dir.find('.'):] == extencion:
        archivos.append(dir)

if len(archivos) == 0:
    print('No existen archivos con la extención', extencion, 'en la carpeta de origen.')
    exit()

print('Copiando archivos con extensión', extencion, 'de', origen, 'a', destino)

for a in archivos:
    # f = open(concat(origen+'\\',a), 'rb') 
    f = open(os.path.join(origen, a), 'rb')
    contenido = f.read(1024 * 1024)
    # d = open(concat(destino+'\\',a), 'wb')
    d = open(os.path.join(destino, a), 'rb') 
    while len(contenido) != 0:
        d.write(contenido)
        contenido = f.read(1024 * 1024)

print('¡Archivos copiados!')
f.close()
d.close()

