"""
Código para muestra de type hints en 
script que imprima un número de veces de
meaw
"""
print("Ejemplo 1: función meaw que impirme la cantidad deseada de meaws")
def meows_1(n: int):
    for _ in range(n):
        print("Meow!")

number: int = int(input("Number: "))
meows_1(number)
print()

#Programación defensiva con docstrings

print("Ejemplo 2: Uso de dostrings en función para imprimir meaw")
def meow_2(n: int) -> str:
    """
    meow_2 n times:

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: in n is not an int
    :rtype: str
    """

    return "meow\n" * n
number = int(input("Number: "))
print(meow_2(number))
print()