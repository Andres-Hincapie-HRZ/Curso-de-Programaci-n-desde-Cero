'''Escribe un programa que solicite al usuario que
ingrese tres números enteros. Luego, calcularán la
suma, el producto y el promedio de estos números.
Recuerden no utilizar librerías externas, funciones,
clases ni condicionales en este ejercicio. Una vez
que hayan completado los cálculos, muestran los
resultados en pantalla.
'''
# Solicitar al usuario que ingrese tres números enteros
num1 = int(input("por favor, Ingresa el primer numero entero: "))
num2 = int(input("ahora, Ingrese el segundo número entero: "))
num3 = int(input("finalmente, Ingrese el tercer número entero: "))

# Calcular la suma, el producto y el promedio
suma = num1 + num2 + num3
producto = num1 * num2 * num3
promedio = (num1 + num2 + num3) / 3

# Mostrar los resultados en pantalla
print("La suma de los tres números es:", suma)
print("El producto de los tres números es:", producto)
print("El promedio de los tres números es:", promedio)