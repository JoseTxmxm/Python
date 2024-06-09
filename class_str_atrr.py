# Archivo de prueba
# Ejemplo de formato de class Student

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Please enter a name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytheryn"]:
            raise ValueError("Please enter a valid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


    def charm(self):
        match self.patronus:
            case "unicorn":
                return "I am a unicorn"
            case "phoenix":
                return "I am a phoenix"
            case _:
                return "I am a human"

def main():
    student = get_studnet()
    student.house = "Number Four, Private Drive"
    #print(f"{student.name} from {student.house}")
    print("Expecto Patronus")
    print(student.charm())# = return: def__str__f" <__main__.Student object at 0x0000014FF077E1B0>
    

def get_studnet():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    patronus = input("Enter your patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

