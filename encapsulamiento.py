#Encapsulamiento del estado del objeto

class Persona():
    def __init__(self, identificacion, nombre, edad):
        self.__identificacion = identificacion#Valor de identificacion oculto
        self.nombre = nombre
        self.edad = edad

#Metodo
    def saludo(self):
        return "Hola " + self.nombre
    
    def getIdentificacion(self):
        return self.__identificacion#Imprimr valor de identificacion oculto
    
    def setIdentificacion(self, valor):#Sobrescribir valor de identificacion
        self.__identificacion = valor


persona1 = Persona(35562345, "Jose", 36)

#print(persona1.identificacion)
#print(persona1._Persona__identificacion)
persona1.setIdentificacion(12345)
print(persona1.getIdentificacion())
print(persona1.nombre)
print(persona1.edad)