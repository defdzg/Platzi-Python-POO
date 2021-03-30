"""
    ABSTRACCIÓN 

Permite enfocarnos en la información relevante.
Separar la información central de los detalles secundarios.
Podemos utilizar variables y métodos (privados o públicos).

"""
class Lavadora:

    def __init__(self):
        pass #Keyword pass, no hay un cuerpo en la función

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Anadiendo jabon')
    
    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == "__main__":

    lavadora = Lavadora()
    lavadora.lavar()