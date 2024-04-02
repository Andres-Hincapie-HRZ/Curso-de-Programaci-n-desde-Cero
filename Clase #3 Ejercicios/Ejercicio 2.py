'''Escribe un programa que solicite al usuario ingresar un número y luego le diga
si ese número es positivo, negativo o igual a cero.'''

# Solicitar al usuario ingresar un número
numero = float(input("Por favor, ingresa un número: "))

# Verificar si el número es positivo, negativo o igual a cero
if numero > 0:
    print("El número ingresado es positivo.")
elif numero < 0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es igual a cero.")