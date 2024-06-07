"""
Función que ingrese en nombre y la 
casa del estudiante
"""


def main():
    student = get_student()
    if student[0] == "Jose":
        student[1] = "Loc La Herraudra"
    elif student[0] == "Balu":
        student[1] = "Airlands"
    elif student[0] == "Kisifur":
        student[1] = "Treehouse"
    elif student[0] == "Tooth":
        student[1] = "Reverside"
    elif student[0] == " ":
        student[1] = "Unknown"
    name1 = get_name()
    house1 = get_house()
    student2 = get_student2()

    print(f"{student[0]} from {student[1]}")
    print(f"{name1} from {house1}")
    print(f"{student2['name2']} from {student2['house2']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


def get_student2():
    student2 = {}
    student2["name2"] = input("Name2: ")
    student2["house2"] = input("House2: ")
    return student2


"""
Ejemplo 2 para la ejecución del
código anterior
"""


def get_name():
    name1 = input("Name1: ")
    return name1


def get_house():
    house1 = input("House1: ")
    return house1


if __name__ == "__main__":
    main()
