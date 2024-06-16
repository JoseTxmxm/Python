"""
Al enumerar los primeros seis números primos 
2, 3, 5, 7, 11 y 13, podemos ver que el sexto primo
es 13
"""

# Encontrar el 10001ésimo número primo

# Funci[on para verificar si un numero es primo]
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    

# Funcion para encontrar el n-esimo numero primo 
def encontrar_numero_esimo_primo(n):
    contador = 0
    numero = 1
    while contador < n:
        numero += 1
        if es_primo(numero):
            contador += 1
    return numero
    

# Encontar el sexto numero primo
milunesimo_primo = encontrar_numero_esimo_primo(10001)
print(f"El milunesimo numero primo es: {milunesimo_primo}")
print()


"""
Ejemplo para encontrar en una secuencia de 1000 los 13 dígitos
adyacentes en el 1000 número de dígitos que tienen el mayor producto
"""
print("Ejemplo mayor producto de 13 en secuencia de 1000 digitos")
# Secuencia de 1000 los 13 dígitos
secuencia = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

# Converitir la secuencia en una lista de enteros
numeros = [int(digito) for digito in secuencia]

# Inicializar el mayor producto
mayor_producto = 0
mejores_digitos = []

# Recorrer la secuencia de números
for i in range(len(numeros) - 12):
    # Tomar trece dígitos adyacentes
    grupo = numeros[i:i+13]

    # Calcular el producto
    producto = 1
    for digito in grupo:
        producto *= digito

    # Comparar con el mayor producto encontrado
    if producto > mayor_producto:
        mayor_producto = producto
        mejores_digitos = grupo

# Mostrar el mayor producto

print(f"El mayor producto de 13 dígitos es: {mayor_producto}")
print(f"Los 13 dígitos son: {mejores_digitos}")
print()

"""
Encontrar el tripe pitagórico en el cual el valor
sumado de a+b+c sea igual a 1000
"""

print("Ejemplo de triple pitagórico que a+b+c sume un total de 1000")

# Encontrar los valore de a, b, y c
def enc_triple_pita(suma_total):
    for a in range(1, suma_total // 3):
        for b in range(a + 1, suma_total // 2):
            c = suma_total - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
            
suma_total = 1000
resultado = enc_triple_pita(suma_total)

if resultado:
    a, b, c = resultado
    print(f"El triple pitagórico para el cual a + b + c = {suma_total} es: ({a}, {b}, {c})")
else:
    print(f"No se encontró un triple pitagórico para el cual a + b + c = {suma_total}")
print()

