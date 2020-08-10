class Producto:
    
    contador_producto = 0
    
    def __init__(self, nombre,precio):
        self.__id_producto = Producto.contador_producto
        self.__nombre = nombre
        self.__precio = precio
        Producto.contador_producto += 1

    def __str__(self):
        return "ID_ nombre: " + str(self.__id_producto)  +" Nombre: "+ self.__nombre + " precio :" + str(self.__precio) 
        
    
    def get_precio(self):
        return self.__precio