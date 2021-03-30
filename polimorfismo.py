"""
    POLIMORFISMO
Habilidad de tomar varias formas.
En python, nos permite cambiar el comportamiento de la
superclase para adaptarlo a la subclase.
"""

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bibicleta')

def main():
    persona = Persona('Daniel')
    persona.avanza()
    ciclista = Ciclista('Miguel')
    ciclista.avanza()


if __name__ == '__main__':
    main()
