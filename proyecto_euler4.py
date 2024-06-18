"""
La suma de los números primos por debajo 
de 10 es 2 + 3 + 5 + 7 = 17
"""

# Encontrar la suma de todos los números primos por debajo de 2 millones
print("Encontrar la suma de todos los números primos por debajo de 2 millones")
limit = 2000000
sieve = [True] * limit
sieve[0] = sieve[1] = False # Por que 0 y 1 no son primos


# Criba de Eratóstenes:
for start in range(2, int(limit**0.5) + 1):
    if sieve[start]:
        for multiple in range(start**2, limit, start): # start*start
            sieve[multiple] = False


# Sumar todos los núemros primos
sum_primes = sum(num for num, is_prime in enumerate(sieve) if is_prime)
print(f"La suma de todos los números primos por debajo de {limit} es: {sum_primes}")
print()

# Función para calcular la suma de los primeros n números naturales
print("Encontrar el primer número triangular que tenga más de quinientos divisores: ")
def count_divisors(num):
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count


def find_triangular_number_with_divisors(min_divisors):
    n = 1
    while True:
        #Calculamos el número triangular
        triangular_number = n * (n + 1) // 2
        #Contamos sus divisores
        if count_divisors(triangular_number) > min_divisors:
            return triangular_number, n
        n += 1

# Encontramos el primer número triangular con más de 599 divisores
triangular_number, n = find_triangular_number_with_divisors(500)
print(f"El primer número triangular con más de 500 divisores es {triangular_number}, que es el {n}-ésimo número triangular.")
print()