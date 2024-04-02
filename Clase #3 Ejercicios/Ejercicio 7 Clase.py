'''Escribe un programa que solicite al usuario ingresar el nombre de un mes y luego indique cuántos días tiene ese mes.'''
# Solicitar al usuario ingresar el nombre de un mes
mes = input("Por favor, ingresa el nombre de un mes: ")
# Verificar la cantidad de días en el mes ingresado
if mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
    print("El mes de", mes, "tiene 31 días.")
elif mes == "febrero":
    print("El mes de febrero tiene 28 o 29 días, dependiendo del año.")
elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
    print("El mes de", mes, "tiene 30 días.")
else:
    print("El mes ingresado no es válido. Por favor, asegúrate de escribir correctamente el nombre del mes.")
