"""
Con el polimorfismo objetos de diferentes clases
pueden ser accedidos utilizando la interfaz, mostrando
un comportamiento distinto (tomando diferentes formas) 
segun sean accedidos.
"""

class Gato():
    def sonido(self):
        print("Miau")

class Perro():
    def sonido(self):
        print("Guau")

class Cerdo():
     def sonido(self):
          print("oing oing")

def escucharSonido(animal):
        animal.sonido()

gato1 = Gato()
perro1 = Perro()
cerdo1 = Cerdo()

escucharSonido(gato1)
escucharSonido(perro1)
escucharSonido(cerdo1)