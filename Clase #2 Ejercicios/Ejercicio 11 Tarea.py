'''
Escribe un programa que solicite al usuario su
nombre, tres notas y los porcentajes
correspondientes para cada una de ellas.
Luego, calcula el promedio ponderado de las
notas según los porcentajes dados y muestra el
resultado junto con el nombre del estudiante.
'''
# Solicitar al usuario su nombre
nombre = input("por favor, Ingresa tu nombre: ")

# Solicitar al usuario las tres notas y sus porcentajes
nota1 = float(input("Ingresa la primera nota: "))
porcentaje1 = float(input("Ingresa el porcentaje de la primera nota: "))

nota2 = float(input("Ingresa la segunda nota: "))
porcentaje2 = float(input("Ingresa el porcentaje de la segunda nota: "))

nota3 = float(input("Ingresa la tercera nota: "))
porcentaje3 = float(input("Ingresa el porcentaje de la tercera nota: "))

# Calcular el promedio ponderado
promedio_ponderado = (nota1 * porcentaje1 + nota2 * porcentaje2 + nota3 * porcentaje3) / (porcentaje1 + porcentaje2 + porcentaje3)

# Mostrar el resultado
print("Nombre:", nombre)
print("Promedio ponderado:", promedio_ponderado)