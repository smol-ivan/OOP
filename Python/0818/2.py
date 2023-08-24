# class Persona:
#     def __init__(self, nombre, dinero):
#         self.__dinero = dinero
#         self.__bolsa = []
#         self.__nombre = nombre
#
#     def getDinero (self):
#         return self.__dinero
#
#     def getBolsa (self):
#         return self.__bolsa
#
#     def getNombre (self):
#         return self.__nombre
#
#     def dineroAlcanza (self, producto):
#         dinero = self.getDinero()
#         if dinero >= producto.getCosto():
#             return True
#         else:
#             return False
#
#     def agregarProducto (self, articulo):
#         articulo = articulo.getArticulo()
#         self.getBolsa().append(articulo)

# class Producto:
#     def __init__(self, articulo, costo):
#         self.__articulo = articulo
#         self.__costo = costo
#
#     def getArticulo (self):
#         return self.__articulo
#
#     def getCosto (self):
#         return self.__costo


# producto_1 = Producto("Galletas Oreo", 20)
# producto_2 = Producto("Panditas Mini", 5)
# producto_3 = Producto("Jugo de Manzana", 10)
#
# productos = [producto_1, producto_2, producto_3]
#
# cliente_1 = Persona("Alberto", 25)
# cliente_2 = Persona("Emi", 5)
#
# clientes = [cliente_1, cliente_2]
#
# def obtenerArticulo ():
#     auth = True
#     while not auth:
#         articulo = input()
#
#
# for j in range(len(clientes)):
#     cliente = clientes[j]
#     if cliente.dineroAlcanza(producto_1):
#         print("Puede comprar el producto")
#         cliente.agregarProducto(producto_1)
#         print(f'{cliente.getBolsa()}')
#     else:
#         print("No le alcanza")

from random import choice


class Producto:
    def __init__(self, articulo, precio):
        self.__articulo = articulo
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def get_articulo(self):
        return self.__articulo


class Persona:
    def __init__(self, nombre, dinero):
        self.__nombre = nombre
        self.__dinero = dinero
        self.__bolsa = []

    def get_nombre(self):
        return self.__nombre

    def get_dinero(self):
        return self.__dinero

    def get_bolsa(self):
        return self.__bolsa

    def agregar_bolsa(self, articulo):
        self.get_bolsa().append(articulo.get_articulo())
        self.__dinero -= articulo.get_precio()


def puede_comprar_producto(persona, articulo):
    return persona.get_dinero() >= articulo.get_precio()


def sort_articulos(*articulos):
    return choice(articulos)


# def comprar(cliente, articulo):
#     cliente.agregar_bolsa(articulo)

def main():
    persona_1 = Persona('Ivan', 20)
    persona_2 = Persona('Hector', 15)
    persona_3 = Persona('Andrea', 30)

    clientes = [persona_1, persona_2, persona_3]

    articulo_1 = Producto('Galletas', 15)
    articulo_2 = Producto('Frituras', 20)
    articulo_3 = Producto('Jugo de Manzana', 10)

    for i in range(len(clientes)):
        cliente = clientes[i]
        articulos = [articulo_1, articulo_2, articulo_3]
        for j in range(len(articulos)):
            articulo = articulos[j]
            if puede_comprar_producto(cliente, articulo):
                print(f'Pudo comprar {articulo.get_articulo()}')
                cliente.agregar_bolsa(articulo)
            else:
                print(f'Sin suficiete dinero')

    print(f'Cliente 1{persona_1.get_bolsa(), persona_1.get_dinero()}')
    print(f'Cliente 2{persona_2.get_bolsa()}')
    print(f'Cliente 3{persona_3.get_bolsa()}')


main()
