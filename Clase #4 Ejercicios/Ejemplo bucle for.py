#Se establecen las variables necesarias
usuario_correcto = "andres"
contraseña_correcta = "123"
intentos_maximos = 3
intentos = 0
#Se crea el ciclo que se repite segun el rango de maximos intentos
for intento in range(intentos_maximos):
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    #Verificar si el usuario ingreso el usuario y la contraseña correcta
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Bienvenido,", usuario)
    else:
        intentos += 1
        print("Usuario y/o contraseña incorrectos. Le quedan", intentos_maximos - intentos, "intentos.")
#Si el usuario  supero los intentos para ingresar  mostrara el siguiente mensaje
if intentos == intentos_maximos:
    print("Demasiados intentos. Por favor, inténtelo más tarde.")