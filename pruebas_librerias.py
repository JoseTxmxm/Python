
import sys
import statistics
from random import choice
import random
"""
coin = random.choice(["cara", "cruz"])
print(coin)
print()
"""

print("Ejecución de random.choice para sinular lanzar una moneda al aire")
coin = choice(["cara", "cruz"])
print(coin)
print()

print("Ejecución de random.choice para imprimir un numero en una longitud de 1 a 10")
number = random.randint(1, 10)
print(number)
print()

print("Ejecución de random.shuffle para simular el azar en las cartas")
cards = ["jack", "King", "queen"]
random.shuffle(cards)
for card in cards:
    print(card)
print()


print("Ejecución de statistics.mean para calcular la media de las cantidades en el bracket")
print(statistics.mean([100, 90]))
print()


print("Ejemplo 1, uso de try, except para manejo de errores con sys.argv")
try:
    print("hello, mi nombre es", sys.argv[1])
except IndexError:
    print("Debes ingresar un nombre")
print()

print("Ejemplo 2, uso de condicionales if, elif, else para manejo de errores con sys.argv")
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, mi nombre es", sys.argv[1])
print()

print("Ejemplo 3, uso de sys.exit para asegurarse de salir antes de que termie la ejecución con sys.argv")
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 4:
    sys.exit("Too many arguments")

print("hello, mi nombre es", sys.argv[1])
print()

print("Ejemplo 4, iterar sobre una lista con un bucle for")
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("Hello, mi nombre es", arg)
print()

print("Ejemplo 5, prueba con slices")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("Hello, mi nombre es", arg)
print()
