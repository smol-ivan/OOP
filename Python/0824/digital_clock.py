class Display_numero:
    def __init__ (self, limite, valor):
        self.__limite = limite
        self.__valor = valor
        
    # Obtener el valor del numero
    def get_valor(self):
        return self.__valor
    
    
    def set_valor(self, valor):
        self.__valor = valor
        
    def incremento(self):
        self.__valor = (self.get_valor() + 1) % self.__limite
        
class Display_reloj:
    def __init__(self, hora = 0, minuto = 0):
        self.__horas = Display_numero(24, hora)
        self.__minutos = Display_numero(60, minuto)
        
    # def get_horas(self):
    #     return self.__horas
    # 
    # def get_minutos(self):
    #     return self.__minutos
    
    def incrementar(self):
        self.__minutos.incremento()
        if (self.__minutos.get_valor() == 0):
            self.__horas.incremento()
            
    def to_string(self):
        return "" + str(self.__horas.get_valor()) + ":" + str(self.__minutos.get_valor())
    
mi_reloj = Display_reloj(23, 59)
mi_reloj.incrementar()
print(mi_reloj.to_string())
