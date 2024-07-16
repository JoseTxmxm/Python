# Practicas de argparse en Python

# Ejemplo con sys en python
"""
Si el usuario no específica el numero 
solo se imprimirá una vez
"""
import sys
import argparse


print("Ejemplo 1 con biblioteca sys")
if len(sys.argv) == 1:
    print("meow")

elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])

    for _ in range(n):
        print("meow")

else:
    print("usage: nueva_prueba.py") # Comprobación del uso del programa


# Ejemplo con argparse en python
print("Ejemplo de con librería argparse en python")
parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
"""
Nota: 
No establecer un nombre de archivo 
con argparse porque podría confundirse 
con la biblioteca que estamos unsando
"""
