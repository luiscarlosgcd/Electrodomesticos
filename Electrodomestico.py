class Electrodomestico:
    def __init__(self, precio, base, color, consumo, peso):
        self.precio = 100 #constante
        self.color = "blanco"
        self.consumo = 'F'
        self.peso = 5 #constante
        self.precioF = self.precioFinal()

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
            self.precioF = self.precio + 100
        elif self.getConsumo() == 'B':
            self.precioF = self.precio + 80
        elif self.getConsumo() == 'C':
            self.precioF = self.precio + 60
        elif self.getConsumo() == 'D':
            self.precioF = self.precio + 50
        elif self.getConsumo() == 'E':
            self.precioF = self.precio + 30
        elif self.getConsumo() == 'F':
            self.precioF = self.precio + 10

        elif 0 <= self.getPeso() <= 19 :
            self.precioF = self.precio + 10
        elif 19 < self.getPeso() <= 49 :
            self.precioF = self.precio + 50
        elif 49 < self.getPeso() <= 79 :
            self.precioF = self.precio + 80
        elif 79 < self.getPeso() :
            self.precioF = self.precio + 100
