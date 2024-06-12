class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickls = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleon, {self.sickls} Sickles, {self.knuts} knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickls + other.sickls
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    

potter = Vault(100, 50, 25)
print("Potter")
print(potter)

weasley = Vault(25, 50, 100)
print("Weasley")
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickls + weasley.sickls
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print("Total Potter + Weasley")
print(total)
print("Ejemplo total2")
total1 = potter + weasley
print(total1)
