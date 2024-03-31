'''
Se requiere desarrollar un programa que permita al
usuario ingresar dos numeros de punto flotante.
El programa realizara diversas operaciones con estos
numeros,como suma,resta,multiplicacion y division.
Luego,mostrara en pantalla los resultados de cada una
de estas operaciones.
'''
numero1 = float(input("Ingrese el primer número de punto flotante: "))
numero2 = float(input("Ingrese el segundo número de punto flotante: "))

# se realiza las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# muestra los resultados
print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la multiplicación es:", multiplicacion)
print("El resultado de la división es:", division)
