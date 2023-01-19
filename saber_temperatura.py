
from tempfile import tempdir
import requests

API_KEY = "*************************************"
ciudad = input("Ingrese el nomnbre de la ciudad: ")

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}")

if r.status_code == 200:
    contenido = r.json()
    print("La temperatura en", ciudad.upper(),"es de", round(contenido['main']['temp']-273.15,2), "grados centígrados")
else:
    print("Ha ocurrido un Error")