'''Escribe un programa que pida al usuario su
nombre, edad y su número favorito multiplica
su edad por su número favorito y muestra por
pantalla el nombre su edad y su edad
multiplicada por su número favorito.
'''
# Solicitar al usuario su nombre

nombre = input("por favor, Ingresa tu nombre: ")

# Solicitar al usuario su edad
edad = int(input("ahora, Ingresa tu edad: "))

# Solicitar al usuario su número favorito
numero_favorito = int(input("finalmente, Ingresa tu número favorito: "))

# Calcular la edad multiplicada por el número favorito
edad_multiplicada = edad * numero_favorito

# Mostrar los resultados
print("Nombre:", nombre)
print("Edad:", edad)
print("Edad multiplicada por tu número favorito:", edad_multiplicada)