'''
Se solicita desarrollar un programa que realice
La suma y la division de dos numeros
especificos,7y 11.Primero,el programa debe
sumar ambos numeros y luego dividir el primer
numero(7)entre el segundo numero (11).
Posteriormente,mostrara en pantalla los
resultados de ambas operaciones,
'''
numero1 = 7
numero2 = 11


suma = numero1 + numero2

division = numero1 / numero2


print("La suma de", numero1, "y", numero2, "es:", suma)
print("La división de", numero1, "entre", numero2, "es:", division)



# Pide al usuario dos números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Suma los números ingresados
suma = numero1 + numero2

# Divide el primer número entre el segundo
division = numero1 / numero2

# Muestra el resultado de la suma y la división
print("La suma de", numero1, "y", numero2, "es:", suma)
print("La división de", numero1, "entre", numero2, "es:", division)