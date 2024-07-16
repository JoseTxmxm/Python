# Generadores, interadores, rendimiento
def main():
    n = int(input("What's n? "))
    for s in bear(n):
        print(s) 

def bear(n):
    flock = [] # flock = lista
    for i in range(n): # i = iterador
        flock.append("oso" * i) # función append() flock.append = añade en lista flock
    return flock # generador en la lista


if __name__ == "__main__":
    main()
