#DECLARAMOS LAS VARIABLES Y SUS VALORES
num1= int(input("Ingresa un numero entero: "))
num2= int(input("Ingrese otro numero entero: "))

# FUNCION SUMAR NUMEROS
def sumar(num1, num2):
    suma = num1 + num2
    #EL RESULTADO QUE RETORNARA LA FUNCION
    return suma

#VARIABLE DONDE SE GUARDARA EL RESULTADO
resultado = sumar(num1,num2)
#IMPRIMIMOS LA FUNCION SUMAR
print(resultado)  
