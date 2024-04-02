'''Escribe un programa que solicite al usuario ingresar tres números enteros
y determine cuál es el mayor de los tres.'''

# Solicitar al usuario ingresar tres números enteros
num1 = int(input("Por favor, ingresa el primer número entero: "))
num2 = int(input("Ahora, ingresa el segundo número entero: "))
num3 = int(input("Finalmente, ingresa el tercer número entero: "))
# Determinar cuál es el mayor de los tres números
if num1 >= num2 and num1 >= num3:
    print("El primer número ingresado:",num1, "es mayor que el segundo",num2," y que el tercer numero", num3)
elif num2 >= num1 and num2 >= num3:
    print("El segundo número ingresado:",num2 ,"es mayor que el primer numero", num1," y que el tercer numero", num3)
else:
    print("El tercer número ingresado:",num3 ,"es mayor que el primer numero", num1, " y que el segundo numero", num2)
