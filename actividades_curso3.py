"""
Escribir un progama que permita
guardar nombres y números de teléfono
"""

#Definir el diccionario con el nombre agenda
agenda = {
    "José": 2345464612,
    "Mario": 2356545751,
    "Angel": 8923561264,
    "Luis": 8903537543,
}

#Definir variable con el nombre consultando con valor True
consultando = True

#Creación de menú sencillo
while consultando:
    print()
    print("MI AGENDA")
    print("---------------------------")
    print("1. Consultar \n2. Añadir \n3. Modificar \n4. Borrar \n5. Salir")

    opcion = ""

    #Define un cilco while y compruebe si la persona ha seleccionado algun numero
    while opcion not in ["1", "2", "3", "4", "5"]:
        opcion = input("-> ")
        
    if opcion == "1":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre esta en el diccionario
        if nombre not in agenda:
            print("El nombre no se encuentra en la agenda")
        else:
            telefono = agenda[nombre]
            print(nombre, ":", telefono)
    
    elif opcion == "2":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre esta en el diccionario
        if nombre in agenda:
            print("El nombre ya se encuentra en la agenda")
        else:
            telefono = int(input("Inrese su teléfono: "))
            #Añadir el telefono a la agenda
            agenda[nombre] = telefono
            print("Contacto agregado")

    elif opcion == "3":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre esta en el diccionario
        if nombre not in agenda:
            print("El nombre no se encuentra en la agenda")
        else:
            telefono = int(input("Inrese su teléfono: "))
            #Modificar el telefono
            agenda[nombre] = telefono
            print("Contacto modificado")

    elif opcion == "4":
        #Pedir nombre
        nombre = input("Nombre: ")
        #Comprobar si el nombre esta en el diccionario
        if nombre not in agenda:
            print("El nombre no se encuentra en la agenda")
        else:
            #Borrar el teléfono
            del agenda[nombre]
            print("Contacto borrado")

    elif opcion == "5":
        consultando = False
        print("Gracias por usar mi agenda")