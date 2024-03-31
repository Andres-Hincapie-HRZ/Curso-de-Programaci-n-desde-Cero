'''Se necesita un programa que pida al usuario dos numeros enteros.
Despues,sumara ambos numeros,Luego dividira el primer numero entre
el segundo mostrara el resultado de la suma y de la division'
Solicitar al usuario que ingrese dos numeros enteros'''

#solicita al usuario que ingrese dos numeros enteros
numero1 = int (input ("Por favor,ingrese el primer numero entero:"))
numero2 = int (input ("Por favor,ingrese el segundo numero entero:"))
#Sumar los dos numeros ingresados
suma = numero1 + numero2
#Dividir el primer numero entre el segundo
division = numero1 / numero2
#Mostrar los resultados de ambas operaciones
print ("El resultado de la suma de es: ", suma)
print("El resultado de dividir es: ", division)