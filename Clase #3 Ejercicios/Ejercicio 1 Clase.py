'''Escribe un programa que pida al usuario ingresar su edad y luego
le diga si es mayor de edad o no.'''

# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si es mayor de edad
if edad >= 18:
    print("¡Eres mayor de edad!")
else:
    print("Eres menor de edad.")
