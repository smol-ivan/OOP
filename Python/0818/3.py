class Masa:
    def _init_(self, tipo, textura, peso):
        self.tipo = tipo
        self.textura = textura
        self.peso = peso

    def calcular_calorias(self):
        modificadores_masa = {
            "Blanca": 1.5,
            "Integral": 1.0,
            "Crujiente": 0.9,
            "Esponjosa": 1.1,
            "Casera": 1.0
        }
        modificador = modificadores_masa.get(self.tipo, 1.0)
        return (2 * self.peso) * modificador


class Ingrediente:
    def _init_(self, tipo, peso):
        self.tipo = tipo
        self.peso = peso

    def calcular_calorias(self):
        modificadores_ingredientes = {
            "Carne": 1.2,
            "Vegetales": 0.8,
            "Queso": 1.1,
            "Salsa": 0.9
        }
        modificador = modificadores_ingredientes.get(self.tipo, 1.0)
        return (2 * self.peso) * modificador


class Pizza:
    def _init_(self, nombre, masa, ingredientes):
        self.nombre = nombre
        self.masa = masa
        self.ingredientes = ingredientes

    def calcular_calorias(self):
        calorias_masa = self.masa.calcular_calorias()
        calorias_ingredientes = sum(ingrediente.calcular_calorias() for ingrediente in self.ingredientes)
        return calorias_masa + calorias_ingredientes


# Crear masas
masa_blanca = Masa("Blanca", "Crujiente", 150)
masa_integral = Masa("Integral", "Esponjosa", 200)

# Crear ingredientes
carne = Ingrediente("Carne", 100)
vegetales = Ingrediente("Vegetales", 50)
queso = Ingrediente("Queso", 75)

# Crear pizza con masas e ingredientes
mi_pizza = Pizza("Mi Pizza", masa_blanca, [carne, vegetales, queso])

# Calcular y mostrar calorías
calorias_totales = mi_pizza.calcular_calorias()
print(f"{mi_pizza.nombre} tiene {calorias_totales:.2f} calorías")