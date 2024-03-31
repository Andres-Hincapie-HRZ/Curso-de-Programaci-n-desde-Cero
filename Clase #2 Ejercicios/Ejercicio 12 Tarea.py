'''"Escribe un programa que te ayude a saber si un número es positivo, negativo o cero. 
Primero, pídele al usuario que te dé un número. Después, verifica si el número que te dio es mayor que 0, menor que 0 o igual a 0.
Si es mayor que 0, dile al usuario que el número es positivo. Si es menor que 0, dile que es negativo. 
Y si es igual a 0, dile que es cero. Finalmente, muéstrale al usuario el resultado.
(Sin usar if, else o elif) 
'''

num = int(input("Ingresa un número: "))
resultado = "positivo" * (num > 0) + "negativo" * (num < 0) + "cero" * (num == 0)
print("El número es", resultado)

num = int(input("Ingresa un número: "))
resultado = "positivo" * (num > 0) + "negativo" * (num < 0) + "cero" * (num == 0)
print("El número es", resultado)

num = int(input("Ingresa un número: "))
resultado = "positivo" * (num > 0) + "negativo" * (num < 0) + "cero" * (num == 0)
print("El número es", resultado)
