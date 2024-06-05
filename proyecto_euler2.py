"""
Función main que calcule la diferencia
de la función suma_cuadrados() y de la
función cuadrado_suma_de_100()
"""
def main():
    resultado_suma_cuadrados = suma_cuadrados()
    resultado_cuadrado_suma_de_10 = cuadrado_suma_de_100()
    result = encontrar_numero_divisible()


"""
Función que encuentra la suma de los cuadrados de los 
primerso 100 números naturales
"""
def suma_cuadrados():
    suma = 0
    for i in range(1, 101):
        suma += i ** 2
    return suma
resultado = suma_cuadrados()


"""
Función que encuentra el cuadrado de la suma de
 los primeros 100 números naturales
"""
def cuadrado_suma_de_100():
    suma = sum(range(1, 101))
    cuadrado_suma = suma ** 2
    return cuadrado_suma


"""
Función que calcula en número más
pequeño que sea divisible entre los números
del 1 al 20 sin ningún resto
"""
def encontrar_numero_divisible():
    numero = 2520
    while True:
        divisible = True
        for i in range(11, 21):
            if numero % i != 0:
                divisible = False
                break
        if divisible:
            return numero
        numero += 2520


result = encontrar_numero_divisible()
resultado_suma_cuadrados = suma_cuadrados()
resultado_cuadrado_suma_de_10 = cuadrado_suma_de_100()
diferencia = resultado_cuadrado_suma_de_10 - resultado_suma_cuadrados

print("El número más pequeño divisble por los números del 1 al 20 es: \n", result)
print("")
print("La suma de los cuadrados de los 100 primeros números naturales es: \n", resultado)
print("")
print("El cuadrado de la suma de los 100 primeros números naturales es: \n", resultado_cuadrado_suma_de_10)
print("")
print("La diferencia entre el cuadrado de la suma de los 100 primeros números es: \n", diferencia)
print("")

if __name__ == "__main__":
    main()


