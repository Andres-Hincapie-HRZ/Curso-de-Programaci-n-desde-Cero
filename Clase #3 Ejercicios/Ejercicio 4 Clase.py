'''Escribe un programa que solicite al usuario ingresar su nombre y luego verifique si el nombre es "Andrés ".Si el nombre es "Andrés ", imprime un mensaje especial de saludo para Andrés ; de lo contrario, imprime un saludo genérico.'''

# Solicitar al usuario ingresar su nombre
nombre = input("Por favor, ingresa tu nombre: ")
# Verificar si el nombre es "Andrés"
if nombre == "Andrés":
    print("¡Hola Andrés! Bienvenido de nuevo.")
else:
    print("Hola", nombre + ". ¡Bienvenido!")

