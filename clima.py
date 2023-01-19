import tkinter as tk
from tkinter import ttk, messagebox
import requests

def obtener():
    API_KEY = "*****************************"
    ciudad = caja1.get()
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}")

    if r.status_code == 200:
        contenido = r.json()
        messagebox.showinfo(
            title="Clima",
            message=f"La temperatura en {ciudad.title()} es de {round(contenido['main']['temp']-273.15,1)} ºC"
        )
        caja1.delete(0, tk.END)
    else:
        messagebox.showinfo(
            title="Clima Error",
            message=f"No se pudo obtener la temperatura de {ciudad.title()}")
        caja1.delete(0, tk.END)
                                                                                                            
ventana = tk.Tk()
ventana.config(width=300, height=250)
ventana.title('Clima')

etiqueta1 = ttk.Label(text="Ingrese una ciudad:")
etiqueta1.place(x=20, y=20)

caja1 = ttk.Entry()
caja1.place(x=20, y=50, width=150, height=20)

boton_obtener = ttk.Button(text='Obtener temperatura', command=obtener)
boton_obtener.place(x=20, y=80)

ventana.mainloop()
