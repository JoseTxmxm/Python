#Práctica en la creación de clases

class Bicicleta():
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin

    #Metodos
    def frenar(self):
        return "La bicicleta está avanzando"
    def avanzar(self):
        return "La bicicleta está en movimiento"
    def girar(self):
        return "La bicicleta está girando"
    
urbana = Bicicleta("Rojo", 5, 26)
hibrida = Bicicleta("Verde", 6, 28)

print("Urbana: " + str(urbana.color))
print("Comportamiento de la bicicleta urbana: " + str(urbana.girar()))
print('\n')
print('Cambios Hibrida: ' + str(hibrida.cambios))
print('Comportamiento de la bicicleta hibrida: ' + str(hibrida.avanzar()))

