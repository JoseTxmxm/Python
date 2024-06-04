# Validación de sin expresiones regulares

import re
print()
print("Validación sin expresiones regulares, ejemplo1")
email = input("¿Cuál es su email? ").strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")
print()

print("Validación sin expresiones regulares, ejemplo2.edu")
email2 = input("Cuál es su email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

print()

# Validación con expresiones regulares de la librería re
print("Uso de la librería re, Ejemplo1.edu")

email3 = input("Cuál es su email? ").strip()

if re.search("@", email3):
    print("Valid")
else:
    print("Invalid")
print()

# Validación con comienzo y final de emparejamientos
print("Validación con comienzo y final de emparejamientos .edu\n"
      " ^ signo de intercalación, indica el incio de la cadena\n"
      "$ representa el final de la cadena\n"
      ". representa cualquier caracter excepto una nueval linea\n"
      "+ indica que el caracter anterior puede aparecer una o más veces\n"
      "* indica que el caracter anterior puede aparecer 0 o más veces\n"
      "? indica que el caracter anterior puede aparecer 0 o 1 vez\n")

email4 = input("Cuál es su email? ").strip()

if re.search(r"^.+@.+\.edu$", email4):
    print("Valid")
else:
    print("Invalid")
print()

# Validación con juego de caracteres, librería re
print("Validación librería re, con juego de caracteres, ejemplo2.org")
email5 = input("Cuál es su email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.org$", email5):
    print("Valid")
else:
    print("Invalid")
print()

# Validación con clases de caracteres, librería re
print("Validación con clases de caracteres, ejemplo3")
print("Agrupación y alternativas")
print(" \"\d\" representa cualquier dígito decimal\n"
      " \"\D\" representa cualquier cosa que no sea un dígito decimal\n"
      " \"s\" representa caracteres de espacio en blanco\n"
      " \"S\" representa cualquier cosa que no sea un caracter en blanco\n"
      " \"w\" representa un carácter de palabra\n"
      " \"W\" es lo opuesto de \"\w\" y representa todo excpeto caracteres de palabra\n")

print("Ejemplo con sensiblidad a mayúsculas, las convierte a minúsculas\n"
      "y manejo de espacios\n")
email6 = input("Cuál es su email? ").strip()

if re.search(r"^(\w|\s)+@\w+\.(com|edu|org|gob|mx)$", email6.lower()):
    print("Valid")
else:
    print("Invalid")
print()

# Explorando las banderas en re.search

print("Validación con ejemplo de re.IGNORECASE que ignora\n"
      "las diferencias entre minúsculas y mayúsculas\n")

email7 = input("¿Cuál es su email? ").strip()

if re.search(r"^\w+@\w+\.(com|edu|org|gob|mx)$", email7, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

print()

# Uso de grupos y operador "?"
print("Validación con uso en ejemplo de operador \"?\" .edu")
email8 = input("¿Cuál es su email? ")

if re.search(r"^\w+@(\w|\s|\.)?\w+\.edu$", email8, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
print()

"""
Especificar la entrada de usuario, especificando
el nombre, en el formato que necesitamos
"""
# Ejemplo sin la librería re
print("Ejemplo formato.py sin la librería re")

nombre = input("Ingrese su nombre: ").strip()

if "," in nombre:
    last, first = nombre.split(", ")
    nombre = f"{first} {last}"
print(f"hello {nombre}")
print()

"""
Capturando grupos con la biblioteca re
buscando el patron last, first
"""
print("Buscando el patron \"last, first\" con la bibliteca re.")

nombre2 = input("¿Cuál es su nombre? ").strip()
matches = re.search(r"^(.+), (.+)$", nombre2)

if matches:
    last, first = matches.groups()
    nombre2 = f"{first} {last}"

print(f"Hola {nombre2}")
print()

# Manipulando grupos con la librería re
print("Ejemplo, manipulando grupos con matches.group()"
      "y control de espacios")
nombre3 = input("¿Cuál es su nombre? ").strip()
matches2 = re.search(r"^(.+), *(.+)$", nombre3)
if matches2:
    nombre3 = matches2.group(2) + " " + matches2.group(1)

print(f"Hola {nombre3}")
print()

"""
Extracción de cadenas y nombre de usuario
"""
print("Ejemplo, extracción de nombre de usuario"
      "con la función removeprefix")

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")  # type: ignore

print(f"Username: {username}")

print()

"""
Extracción de cadenas y nombre de usuario
con la funcion re.sub de la librería re
"""
print("Ejemplo, extracción de nombre de usuario con"
      "la función re.sub de la librería re")

url2 = input("URL: ").strip()

username2 = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url2)

print(f"Username: {username2}")
print()

"""
Extracción de datos de grupo con la función
re.search de la libreria re
"""
print("Ejemplo, extracción de datos de grupo con re.search")
print("Uso del operador warlus")

url3 = input("URL: ").strip()

if matches3:= re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url3, re.IGNORECASE):
    print(f"Username: ", matches3.group(1))
print()

"""
Mismo ejemplo anterios limitandose a letras, 
números y guiones bajos
"""
print("Mismo ejemplo anterior limintandose a letras,"
      " números y guiones")

url4 = input("URL: ").strip()

if matches4:= re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url4, re.IGNORECASE):
    print("Username:", matches4.group(1))
print()
