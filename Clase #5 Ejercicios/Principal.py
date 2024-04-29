# En un archivo llamado Principal.py

from suma import sumar

# Pedir al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamar a la función sumar para sumar los números ingresados por el usuario
resultado = sumar(num1, num2)

# Mostrar el resultado al usuario
print("La suma de", num1, "y", num2, "es igual a:", resultado)


