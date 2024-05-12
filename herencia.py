"""La herencia son los atributos heredados de las clases padres
 o super a las clases hijas o subclase
 """

class Vehiculo():
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula  
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False

    def avanzar(self):
        self.avanza = True

    def frenar(self):
        self.frena = True

    def girar(self):
        self.gira = True

    def imprimir(self):
        print(f'Matricula: {self.matricula} \n Modelo: {self.modelo} \n Marca: {self.marca} \n Color: {self.color} \n'
              f'Avanzar: {self.avanza} \n Fenar: {self.frena} \n Girar: {self.gira}')
 
class Moto(Vehiculo):
    #pass para heredar directamente todos los atributos de la clase padre
    def __init__(self, matricula, modelo, marca, color, cilindraje):#Para agregar atributos a la clase hija
        super().__init__(matricula, modelo, marca, color,)#Para heredar los atributos del metodo de la clase padre
        self.cilindraje = cilindraje

moto1 = Moto("ABC234", 2027, "Yamaha", "Verde", 350)


moto1.avanzar()
moto1.girar()
moto1.frenar()
print("Cilindraje: " + str(moto1.cilindraje))
moto1.imprimir()

