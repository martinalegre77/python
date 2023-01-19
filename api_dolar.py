# Servicios Web
import requests

r = requests.get("https://api.recursospython.com/dollar")

if r.status_code == 200:
    print('Peticion exitosa')
    contenido = r.json()
    print("Precio Dolar para la Compra: ", contenido['buy_price'])
    print("Precio Dolar para la Venta: ", contenido['sale_price'])
else:
    print("Error, no se pudo obtener la información")