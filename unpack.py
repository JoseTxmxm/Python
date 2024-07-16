# Practicas de desempaquetado de listas y diccionarios en python

first, _ = input("Whats's your name? ").split(" ")
print(f"hello, {first}\n")


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# coins = [100, 50, 25]
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(100, 50, 25), "knuts")
# print(total(coins[0], coins[1], coins[2]), "knuts") typeError
# print(total(*coins), "knuts")
# print(total(galleons=100, sickles=50, knuts=25), "knuts")
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
print(total(**coins), "knuts\n")

# Ejemplo 2 de argumentos posicionales


def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


f(100, 50, 25, 5)
f(galleons=100, sickles=50, knuts=25)
print()

# Ejemplo con función map()
print("Ejemplo de diferencias de append() y map()\n")


def main():
    yell("This", "is", "CS50")
    yell2("Soy", "Estudiante", "De", "Programación")
    yell3("Estudio", "En", "Edutin", "Academy")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


def yell2(*words2):
    uppercased2 = map(str.upper, words2)
    print(*uppercased2)


def yell3(*words3):
    uppercased = [word.upper() for word in words3]
    print(*uppercased)


if __name__ == "__main__":
    main()
