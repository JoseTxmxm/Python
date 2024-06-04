import re
# Maniulacion de grupos con librería re
print("Buscando el patron \"last, first\" con la bibliteca re.")

nombre2 = input("Ingrese su nombre:")

if matches:= re.search(r"^(.+),(.+)$", nombre2):
    nombre2 = matches.group(2)+" "+matches.group(1)

print(f"Hola {nombre2}")
print()
