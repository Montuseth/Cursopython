class Orden:
    
    contador_de_ordenes = 0
    
    def __init__(self,productos):
        self.__id_orden = Orden.contador_de_ordenes
        self.__productos = productos
        Orden.contador_de_ordenes +=1
    
    def __str__(self):
        productos_str = ""
        for productos in self.__productos:
            productos_str += productos.__str__() + "|"
        
        return "Id orden : " + str(self.__id_orden) + " Productos = " + productos_str
    
    def agregar_producto(self,productos):
        self.__productos.append(productos)
        
    def calcular_total(self):
        total = 0;
        for producto in self.__productos:
            total += producto.get_precio()
        return total
    
        
             
    
    

    