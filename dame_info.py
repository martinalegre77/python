# Buscador de noticias

import pprint
import requests

API_KEY = '********************************'
info = input('Sobre qué deseas información? ')
r = requests.get(f"https://newsapi.org/v2/everything?q={info}&from=2023-01-16&sortBy=publishedAt&apiKey={API_KEY}")

if r.status_code == 200:
    print('Peticion exitosa')
    contenido = r.json()
    pprint.pprint(contenido)
    # print(contenido['title'])
    # print(contenido['description'])
    # print(contenido['author'])
else:
    print("Error, no se pudo obtener la información")