'''
Solicita al usuario que ingrese un numero entero y
luego determina si es par o impar.Muestra el
resultado
(Sin usar if, else o elif)'''

numero= int(input ("Ingrese un numero entero:"))

resultado= "par" *(numero % 2 == 0) +"impar"*(numero % 2 != 0)

print ("El numero ingresado es",resultado)