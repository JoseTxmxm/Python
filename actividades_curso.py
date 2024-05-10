"""
ESTRUCTURA ACTIVIDAD OPERACIONES
Implementar un programa que realice operaciones báscias,
como ingresar y devolver datos por consola,
así como utilizar operadores aritméticos y lógicos
"""

#Pedir números al usuario

primer_numero = int(input("Ingresa un número (1): " ))
segundo_numero = int(input("Ingresa un segundo número (2): " ))

#Realizar las operaciones aritméticas
print(f'La suma es: {primer_numero + segundo_numero}')
print(f'La multiplicación es: {primer_numero * segundo_numero}')

#Operaciones de comparación
print(f'¿Los números son iguales?: {primer_numero == segundo_numero}')
print(f'¿El primer número es mayor o igual al primero?: {segundo_numero < segundo_numero}')
print(f'¿El segundo número es mayor o igual al primero?: {segundo_numero >= primer_numero}')

"""
ESTRUCTURA ACTIVIDAD CONDICIONALES
Crear un programa que integre descuentos a los clientes en navidad,
de acuerdo al monto de su compra imprima en consola
el nombre del cliente, valor de la compra sin descuento
valor de la compra con descuento
"""

#Solicitar información

nombre = input("Ingrese el nombre del cliente: ")
valor_compra = float(input("Ingrese el valor de la compra: "))

#Establecer condiciones

if valor_compra <80:
    print(f'Hola, {nombre}. El valor a pagar es: $ {valor_compra}')
elif 80 <= valor_compra < 150:
    descuento = 0.1
elif 150 <= valor_compra < 300:
    descuento = 0.15
elif 300 <= valor_compra <= 500:
    descuento = 0.2

#Obtenga el precio final usando la formula indicada en el problema
precio_final = valor_compra - (valor_compra * descuento)

#Imprima los resultados
print(f"Compra sin descuento: {valor_compra}. Compra con descuento: {precio_final}" )

"""
ESTRUCTURA ACTIVIDAD CICLOS
Escribe un programa que solicite tu nombre completo,
el nombre de las cinco materias y las calificaciones de
cada una. Y como resultado devuelve tu nombre y el promedio obtenido
en el semestre
"""

#Solicitar informacion

name = input("Nombre completo: ")
materias = 5

#Hacer un ciclo, pedir datos y sumar la calificacion
contador = 1
sumatoria = 0

while contador <= materias:
    nombre_materia = input("Ingresa el nombre de la (" +str(contador) +") materia: ")
    calificacion = float(input("Calificaciones obtenidas en: " + str(nombre_materia) + ": "))

#Sumar la calificacion a la sumatoria
    sumatoria = sumatoria + calificacion

#Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1


#Hacer calculos e imprimir resultados
promedio = sumatoria / materias
print("***RESULTADOS***")
print(f'Hola, {nombre} tienes un promedio de {promedio} en el 5to semestre.')