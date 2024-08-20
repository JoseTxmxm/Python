"""
Crear un programa conversor de monedas 
que permita conocer el valor de euros a 
yuanes, pesos colombianos y libras esterlinas
"""

print("Bienvenidos al conversor de monedas")

#Definicion de la funcion principal con sus parametros
def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:
#Subfuncion a ejecutar si se selecciono 1 para convertir a dolares
        def dolarTo():
            if moneda_actual == "1":
                print(f'{valor} dolares equivalen a ${valor * 3750} pesos colombianos')
            elif moneda_a_convertir == "2":
                print(f'${valor} dolares equivale a Y{valor * 6.37} yuanes')
            elif moneda_a_convertir == "3":
                print(f'${valor} dolares equivales a £{valor * 0.76} libras esterlinas')
            else:
                print("No se reconoce la moneda_a_convertir")

        dolarTo()

    elif moneda_a_convertir == "1":

#Subfuncion a ejecutar si se selecciono 2 para convertir a euros
        def euroTo():
            if moneda_a_convertir == "2":
                print(f'E{valor} euros equivales a ${valor * 4000} pesos colombianos')
            elif moneda_a_convertir == "2":
                print(f'E{valor} euros equivale a Y{valor * 6.93} yuanes')
            elif moneda_a_convertir == "3":
                print(f'E{valor} euros equivales a ${valor * 0.83} libras esterlinas')
            else:
                print("No se reconoce la moneda_a_convertir")

        euroTo()

    else:
        print("No se reconoce la moneda_a_convertir")

# Variable que almacena valor de (1) para dolar y (2) para euro.
moneda_actual = int(input("Ingrese su moneda actual: \n 1. Dolar \n 2. Euro \n"))

#Pedir cantidad de dolares o euro a convertir
valor = float(input("Ingrese el valor a convertir: \n"))

#Indique a que valor quierer convertir la moneda
moneda_a_convertir = input(
    "¿A qué moneda quiere conertirlo \n 1. Pesos colombianos"
    "\n 2. Yuanes \n 3. Libras Esterlinas \n")

"""
Invoque la funcion y envie los valores almacenados
en las variables moneda_actual, valor y moneda_a_convertir
"""
conversor(moneda_actual, valor, moneda_a_convertir)
