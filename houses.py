"""
Exploración de conjunto de datos de estudiantes
en la lista
Imprime la casa de los estudiantes en la lista
"""
print(
    "Ejemplo 1, extracción de datos con script de conjutno en una lista\n"
    "Imprime la lista en orden alfabético"
    )

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
print()

"""
Creación de un script que 
usa el valor de variables constantes
para impirimir tres veces el maullido de un 
gato.
Creación de clase 
"""
print("Ejemplo 2, imprime tres veces meow")
for _ in range(3):
    print("Meow!")
print()
print("Segunda versión del ejemplo 2, constante en mayúsculas")

MEOW_COUNT = 3
for _ in range(MEOW_COUNT):
    print("Meow!")
print()

"""
Creación de código Python que contiene la 
class Account: Uso de variables globales
    que define un balance, deposit, withdraw,
    realiza las operaciones correspondientes,
    imprime en pantalla el balance total en account,
    se hace uso de @propertys y setters para
    controlar el balance de la cuenta.
    """
print("Ejemplo 3, creación de class Account\n"
      "para realizar las operaciones correspondientes\n"
      "con la cuenta bancaria e imprimir el balance de la cuenta")
class Account:
    def __init__(self):
        self._balance = 0


    @property
    def balance(self):
        return self._balance
    

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    account._balance = 1000
    print("Balance:", account._balance)
    account.deposit(100)
    account.withdraw(50)
    print("Total in account:", account._balance)

if __name__ == "__main__":
    main()

print(type(Account))# type: ignore

