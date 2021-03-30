"""
    DEFINICIÓN DE CLASE 

class <nombre_de_la_calse>(<super_clase>): #La clase es un molde

    #Keyword def (funciones)
    #Las funciones dentro de las clases se llaman **métodos**

    def __init__(self, <parameters>) #El contstructor
        <expresión>

    def <nombre_del_metodo>(self, <parameters>): 
        <expresion>
"""

""" 
    EJEMPLO DE CLASE
#Clase
class Persona: 

    # Todos los métodos de una clase reciben implicitamente
    como primer parámetro *self*

    # Constructor
    def __init__(self, nombre, edad): # Método
        self.nombre = nombre        #Instancia
        self.edad = edad            #Instancia

    def saluda(self, otra_persona): # Método
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}.'
"""
# Para definir una variable privada, se utilizan **convenciones**
# Se comienza con " _ "

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre #Atributos, se accede a ellos con la notación punto
        self.edad = edad

    def saluda(self, otra_persona):
        return print(f'Hola {otra_persona.nombre} me llamo {self.nombre}.')

daniel = Persona('Daniel',22)
marcela = Persona('Marcela', 40)

daniel.saluda(marcela)
