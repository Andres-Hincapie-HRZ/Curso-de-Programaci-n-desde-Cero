'''
Se requiere desarrollar un programa que solicite al
usuario ingresar su nombre y su edad.Posteriormente.
el programa calculara la edad ingresada por el usuario
elevada al cubo.Finalmente,mostrara en pantalla el
nombre del usuario junto con el resultado de elevar su
edad al cubo.
'''


# Solicitar al usuario que ingrese su nombre y edad
nombre = str(input("Ingrese su nombre: "))
nombre2 = input("ingrese su segundo nombre: ")
edad = int(input("Ingrese su edad: "))

# Calcular la edad elevada al cubo
edad_cubo = edad ** 3

# Mostrar el resultado
print(f"{nombre}, el resultado de elevar tu edad al cubo es: {edad_cubo}")
