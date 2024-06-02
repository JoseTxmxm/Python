"""
Encuentra la suma de todos los 
múltiplos de 3 o 5 por debajo de 1000
"""
print()
print("multiplos de 3 o 5 por debajo de 1000")


def suma_multiplos_3_o_5(n):
    suma = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma


"""
Calculamos la suma de todos los múltiplos de 3 
o 5 por debajo de 1000
"""
resultado = suma_multiplos_3_o_5(1000)
print("La suma de todos los múltiplos de 3 o de 5 por debajo de 1000 es: ", resultado)
print()

"""
Resolución 2 de problema de números de
Fibonacci"""
print("Resolucion 2 de problema de números de Fibonacci")


def suma_fibonacci_pares_limite(limite):
    sum = 0
    a, b, = 1, 2
    while a <= limite:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum


limite = 4000000
resultado = suma_fibonacci_pares_limite(limite)
print("La suma de los terminos pares de la secuencia de Fibonacci menores o iguales a",
      limite, "es: ", resultado)
print()

"""
Crea un programa en Python para 
encontrar el factor primo del numero:
600851475143
"""
print("Encontrar el mayor factor primo del numero 600851475143")
def mayor_factor_primo(numero):
    factor = 2
    while factor * factor <= numero:
        if numero % factor == 0:
            numero //= factor
        else:
            factor += 1
    return numero

numero = 600851475143

resultado = mayor_factor_primo(numero)

print("El mayor factor primo de", numero, "es: ", resultado)
print()

"""
Crea una clase para encontrar el palindromo mas grande 
hecho del producto de dos secuencias
de 3- numeros digitos"""

print("Clase para encontrar el palindromo "
      "mas grande hecho del producto de dos secuencias "
      "de 3- numeros digitos")
class PalindromoMasGrande:
    def __init__(self):
        self.palindromo_mas_grande = 0
        self.factor1 = 0
        self.factor2 = 0

    def es_palindromo(self, numero):
        return str(numero) == str(numero)[::-1]
    
    def encontrar_palindromo_mas_grande(self):
        for i in range(100, 1000):
            for j in range(100, 1000):
                producto = i * j
                if self.es_palindromo(producto) and producto > self.palindromo_mas_grande:
                    self.palindromo_mas_grande = producto
                    self.factor1 = i
                    self.factor2 = j
        return self.palindromo_mas_grande, self.factor1, self.factor2
    
# Uso de la clse
palindromo = PalindromoMasGrande()
palindromo.encontrar_palindromo_mas_grande()
resultado, factor1, factor2 = palindromo.encontrar_palindromo_mas_grande()
print("El resultado mas grande hecho del producto de "
      "dos numeros de 3 digitos es: ", resultado)
print("Se obtiene multiplicando", factor1, "y", factor2)
print()
