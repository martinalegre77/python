# Crear clase Producto
# Atributos:
#   - Nombre (cadena)
#   - Precio (número de coma flotante)
#   - Stock (número entero)
# Métodos:
#   - efectuar_venta(cantidad: int)
#       - Si hay suficiente stock, resta la cantidad indicada como argumento.
#       - Si no hay suficiente stock (o sea, si stock > cantidad), lanza
#         ValueError.

# Luego de definir la clase, el siguiente código debe imprimir
# el resultado correspondiente:

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = str(nombre)
        self.precio = float(precio)
        self.stock = int(stock)

    def efectuar_venta(self, cantidad):
        if(self.stock > cantidad):
            self.stock-=cantidad
        else:
            raise ValueError('No hay stock suficiente') 
        
mouse = Producto("Mouse", 2000, 10)
print(mouse.stock)  # Imprime 10
mouse.efectuar_venta(1)   # Recibe como argumento la cantidad de mouses vendidos.
print(mouse.stock)  # Imprime 9
teclado = Producto("Teclado", 5000, 1)
print(teclado.stock)  # Imprime 1
teclado.efectuar_venta(2)   # Lanza (raise) ValueError (no hay stock suficiente)
