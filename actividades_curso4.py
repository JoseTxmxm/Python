"""
Implementar un programa con una clase llamada Persona que contenga
los atributos que serán ingresado por teclado: nombre y edad. Un 
método llamado impromir que devuelva el nombre y la dedad.
Crear una clase llamada Ciudadadno que herede la clase Persona y agregue
un atributo llamado depósito que será ingresado por teclado.
Crear un método llamado impuestos y si el depósito es superior a 4000 USD
muestre que SI debe pagar, caso contrario no deberá pagar.
"""
#Crear la clase Persona
class Persona:

    def __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.edad = int(input('Ingrese su edad: '))

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

#Crear la clase Ciudadano
class Ciudadano(Persona):

    def __init__(self):
        super().__init__()
        self.deposito = float(input('Ingrese su depósito: '))

    #Definir el método imprimir
    def imprimir(self):
        super().imprimir()
        print("Depósito:", self.deposito)

    #Definir el método impuestos
    def impuestos(self):
        if self.deposito > 4000:
            print(f'El ciudadano {self.nombre} debe pagar impuestos')
        else:
            print(f'El ciudadano {self.nombre} no debe pagar impuestos')

#Crear un objeto de la clase Ciudadano1 y llame a los métodos imprimir e impuestos
ciudadano1 = Ciudadano()

ciudadano1.imprimir()

ciudadano1.impuestos()