from math import sqrt, acos

class Vector:
    
    def __init__(self, x, y, z):
        self.vector = [x, y, z]

    def magnitud(self):
        return sqrt((self.vector[0]**2) + (self.vector[1]**2) + (self.vector[2]**2))
    
    def sumar(self, v):
        x = self.vector[0] + v[0]
        y = self.vector[1] + v[1]
        z = self.vector[2] + v[2]
        return [x, y, z]
    
    def producto_punto(self, v):
        acum = 0
        for i in range(len(self.vector)):
            acum = self.vector[i] * v[i] + acum
        return acum

    def angulo(self,v):
        producto = self.producto_punto(v)
        magnitud = self.magnitud()
        return acos(producto/magnitud)

vectorPrueba = Vector(1, 1, 1)
v = [2, 2, 2]

# print(f'Magnitud: {vectorPrueba.magnitud()}')
# print(f'Sumar vectores: {vectorPrueba.sumar(v)}')

# print(f'Prodcuto punto {vectorPrueba.producto_punto(v)}')

print(f'Angulo {vectorPrueba.angulo(v)}')

