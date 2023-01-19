# Realizar un script para copiar un archivo a 
# partir de un archivo ya creado (.txt)
# ingrese el archivo de origen
# ingrese el archivo de destino
# copiando los datos de hola.txt a destino.txt
# ¡datos copiados!

origen = input('Ingrese el nombre del archivo de origen: ')
destino = input('Ingrese el nombre del archivo de destino: ') 

print('Copiando los datos de ', origen, ' a ', destino, '...')

f = open(origen, 'r', encoding='utf8') 
contenido = f.read()
f.close()

f = open(destino, 'w', encoding='utf8') 
f.write(contenido)
f.close()

print('¡Datos copiados correctamente!')

