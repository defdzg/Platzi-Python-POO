"""
    HERENCIA
Permite modelar una jerarquía de clases.
Permite compartir comportamiento común en la jerarquía.
Al padre se le conoce como superclase y al hijo como subclase.

"""
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    
    def __init__(self,lado):
        #Nos permite obtener una referencia directa de la superclase
        #Heredamos el método área de la superclase a la subclase
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area()) #Estamos heredando el método área de nuestra superclase