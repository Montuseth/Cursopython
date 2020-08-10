from producto import Producto
from orden import Orden

producto1 = Producto("Camisa", 1000)
producto2 = Producto("zapatilla", 1300)
producto3 = Producto("tije", 1300)


productos = [producto1,producto2];

print(productos)
orden1 = Orden(productos)
#orden1.agregar_producto("prueba 1", 300)
print(orden1)
orden1.agregar_producto(producto3)
print("Total :" , orden1.calcular_total())