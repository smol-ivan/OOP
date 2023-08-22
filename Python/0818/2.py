class Persona:
    def __init__(self, nombre, dinero):
        self.__dinero = dinero
        self.__bolsa = []
        self.__nombre = nombre
        
    def getDinero (self):
        return self.__dinero
    
    def getBolsa (self):
        return self.__bolsa
    
    def getNombre (self):
        return self.__nombre
    
    def dineroAlcanza (self, producto):
        dinero = self.getDinero()
        if dinero >= producto.getCosto():
            return True
        else:
            return False
    
    def agregarProducto (self, articulo):
        articulo = articulo.getArticulo()
        self.getBolsa().append(articulo)
    
class Producto:
    def __init__(self, articulo, costo):
        self.__articulo = articulo
        self.__costo = costo
        
    def getArticulo (self):
        return self.__articulo
    
    def getCosto (self):
        return self.__costo
        

producto_1 = Producto("Galletas Oreo", 20)
producto_2 = Producto("Panditas Mini", 5)
producto_3 = Producto("Jugo de Manzana", 10)

productos = [producto_1, producto_2, producto_3]

cliente_1 = Persona("Alberto", 25)
cliente_2 = Persona("Emi", 5)

clientes = [cliente_1, cliente_2]

def obtenerArticulo ():
    auth = True
    while not auth:
        articulo = input()
        

for j in range(len(clientes)):
    cliente = clientes[j]
    if cliente.dineroAlcanza(producto_1):
        print("Puede comprar el producto")
        cliente.agregarProducto(producto_1)
        print(f'{cliente.getBolsa()}')
    else:
        print("No le alcanza")
        