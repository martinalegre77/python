# Desarrollar un pequeño programa anti-spam. 
# La base de datos es un extracto de una base de datos real. Algunos de esos usuarios son spam. 
# El objetivo del programa es detectar cuáles son, imprimiendo cada uno en pantalla. 
# Consuman el servicio web IP-API (documentación en https://ip-api.com/docs/api:json) para 
# conocer el país de origen de cada usuario según la dirección de IP con que se 
# registraron en el foro (campo "regip" de la base de datos). Los usuarios cuya IP 
# pertenezcan a alguno de los siguientes países deben ser considerados spam (en un 
# escenario real habría que chequear además otras variables):

#     Ucrania
#     Polonia
#     Finlandia

import os
import sqlite3
import requests

os.system("cls") 

conn = sqlite3.connect('mybb.db')
cursor = conn.cursor()

try:
    cursor.execute('SELECT * FROM users')
except sqlite3.OperationalError:
    print('No se pudo leer la Base de Datos')
    exit()

usuarios = cursor.fetchall()
paisSpam = ['Ukraine', 'Poland', 'Finland']

for id, username, regip in usuarios:
    r = requests.get(f"http://ip-api.com/json/{regip}")
    if r.status_code != 200:
        print("Ups! Ha ocurrido un error")
    else:
        contenido = r.json()
        pais = contenido['country']
        if pais in paisSpam:
            print(f'El usuario {username} de {pais} es SPAM')

conn.close()