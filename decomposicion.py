"""
DECOMPOSICIÓN

    Partir un problema en problemas más pequeños.

    Las clases permiten crear mayores abstracciones en forma de componentes.

    Cada clase se encarga de una parte del problema y el programa se vuelve 
    más facil de mantener. 

"""

class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo' #Variable privada
        self._motor = Motor(cilindros=4) #Variable privada

    def acelarar(self, tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'
        print(self._estado)

class Motor:

    def __init__(self, cilindros, tipo='gasolina'): #Default keyword
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        print(self.tipo)

    def inyecta_gasolina(self, gasolina):
        self.gasolina = gasolina
        print(self.gasolina)
        pass
        
if __name__ == "__main__":

    #Instancias
    tesla = Automovil('roadster', 'tesla', 'rojo')
    tesla.acelarar(tipo='rapido')
    tesla._motor = Motor(cilindros=4, tipo='electrico')