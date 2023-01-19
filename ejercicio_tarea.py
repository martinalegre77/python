# Saber cuales procesos estan usando más de esa memoria

import subprocess

memoria = int(input('Ingrese una cantidad de memoria (en KB): '))

p = subprocess.run('tasklist', capture_output=True, encoding='cp850')

salida = p.stdout.strip()
lineas = salida.split('\n')
lineas = lineas[2:]

for linea in lineas:
    linea = linea.strip()
    nombre_proceso = linea[0:25].strip()
    uso_memoria = linea[-12:-3].strip()
    uso_memoria = int(uso_memoria.replace('.',''))
    if uso_memoria > memoria: 
        print(f'{nombre_proceso} está usando {uso_memoria} KB de memoria')