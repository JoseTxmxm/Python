# Ejercicios comprension de listas
print("Ejercicios comprension de listas")
print("Ejemplo 1")
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
print()

print("Ejemplo 2,uso de función filter() y función list()")


def is_gryffindor(s):
    """
    if s|["house"] == "Gryffindor":
        return True
    else:
        return False
    """
    return s["house"] == "Gryffindor"


gryffindor = filter(is_gryffindor, students)  # filter(función, iterable)
gryffindor = list(gryffindor)
print(gryffindor)
print()

# Ejemplo 3, dictionary comprehension
print("Ejemplo 3, uso de dict comprehension")
students2 = ["Hermione", "Harry", "Ron"]

gryffindor2 = []

for student in students2:
    gryffindor2.append({"name": student, "house": "Gryffindor"})
print(gryffindor2)
print()

# Ejemplo 4, list comprehension
print("Ejemplo 4, ditcionary comprehension")
gryffindor3 = [{"name": student, "house": "Gryffindor"}
               for student in students2]
print(gryffindor3)

# Ejemplo 5, list comprehension
print("Ejemplo 5, ditcionary comprehension")
gryffindor3 = {student: "Gryffindor" for student in students2}
print(gryffindor3)
print()

# Ejemplo 6, list comprehension, uso de la función enumerate(iterable, start=0)
print("Ejemplo 6, ditcionay comprehension, uso de la función enumerate()")
for i, student in enumerate(students2, start=0):# enumerate(iterable, start=0)
    print(i + 1, student)
print()
