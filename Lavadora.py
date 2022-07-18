from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __innit__(self, precio, base, color, consumo, peso, carga):
        super().__init__(self, precio, base, color, consumo, peso)
        self.precioF = self.precioFinal()
        self.carga = 5
    
    def setCarga(self, carga):
        self.carga = carga

    def getCarga(self):
        return self.carga
    
    def precioFinal(self):
        super().precioFinal(self)
        if self.carga > 30: self.precioF += 50