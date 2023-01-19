
from tempfile import tempdir
import requests

API_KEY = "ad5fa90757c9ab691f25ae08f22a3e19"
ciudad = input("Ingrese el nomnbre de la ciudad: ")
# ciudad = "concordia"
r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}")
 
if r.status_code == 200:
    contenido = r.json()
    print("La temperatura en", ciudad.upper(),"es de", round(contenido['main']['temp']-273.15,2), "grados centígrados")
else:
    print("Ha ocurrido un Error")

# si no lo podes hacer en dos pasos:
# main = contenido["main"]
# temp = main["temp"]

# https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin

# https://rapidapi.com




