# Class hat = sombrero clasificador
import random

#class Hat:
    #def __init__(self):
    #    self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#classmethod
def sort(name):# self se reemplaza por cls
    print(name, "is in", random.choice(houses))# self.houses se reemplaza por cls


#hat = Hat()
#hat.sort("Harry")
#Hat.sort("Harry")

sort("Harry")