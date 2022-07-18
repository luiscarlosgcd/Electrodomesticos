class Electrodomestico:
    def __init__(self, precio, base, color, consumo, peso):
        self.precio = 100 #constante
        self.color = "blanco"
        self.consumo = 'F'
        self.peso = 5 #constante

    def setPrecio(self, precio): #getter y setter para precio
        self.precio = precio
    
    def getPrecio(self):
        return self.precio

    def setColor(self, color):
        self.color = color
        self.comprobarColor()
    
    def getColor(self):
        return self.color

    def setConsumo(self, consumo):
        self.consumo = consumo
        self.comprobarConsumo()
    
    def getConsumo(self):
        return self.consumo

    def setPeso(self, peso):
        self.peso = peso
    
    def getPeso(self):
        return self.peso

    def comprobarColor(self): #comprobadores para la clase para crear validaciones
        if (self.color != 'blanco' or 'negro' or 'rojo' or 'azul' or 'gris'):
            self.color = 'blanco'
    
    def comprobarConsumo(self):
        if (self.consumo == ('A' or 'B' or 'C' or 'D' or 'E', 'F')):
            self.consumo = 'F'

    def precioFinal(self):
        if self.getConsumo() == 'A':
            