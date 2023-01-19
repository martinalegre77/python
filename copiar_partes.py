# COPIAR POR FRAGMENTOS

while True:
    try:
        file_origen = input('Ingrese el nombre y extención del archivo de origen: ')
        f_o = open(file_origen, 'rb')
    except FileNotFoundError:
        print("El archivo de origen no existe")
    else:
        break
    
file_destino = input('Ingrese el nombre y extención del archivo de destino: ')

print('Copiando los datos de ', file_origen, ' a ', file_destino, '...')

contenido = f_o.read(1024 * 1024)

f_d = open(file_destino, 'wb')

while len(contenido) != 0:
    f_d.write(contenido)
    contenido = f_o.read(1024 * 1024)

print('¡Archivo copiados correctamente!')
f_o.close()
f_d.close()
        





    
    
   
    
    

