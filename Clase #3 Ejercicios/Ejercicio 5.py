'''Escribe un programa que solicite al usuario ingresar un número entero
e indique si es par o impar.'''

# Solicitar al usuario ingresar un número entero
numero = int(input("Por favor, ingresa un número entero: "))
# Verificar si el número es par o impar
if numero % 2 == 0:
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar.")