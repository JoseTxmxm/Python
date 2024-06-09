# Ejemplo de formato de class Student

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


# Getter
    @property
    def name(self):
        return self._name

# Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Please enter a name")
        self._name = name

# Getter
    @property
    def house(self):
        return self._house


# Setter 
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytheryn"]:
            raise ValueError("Please enter a valid house")
        self._house = house

def main():
        student = get_studnet()
        #student._house = "Number four, Privet Drive"
        #print(f"{student.name} from {student.house}")
        print(student)# = return: def__str__f" <__main__.Student object at 0x0000014FF077E1B0>
    

def get_studnet():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
