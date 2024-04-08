

usuario_correcto= "andres"
contraseña_correcta= 123

usuario= input("Digite su Usuario: ")
contraseña= input("Digite su contraseña: ")

while usuario != usuario_correcto or contraseña != contraseña_correcta: 
    print("Usuaruio y contraseña incorrecta")
    usuario= input("Digite su Usuario: ")
    contraseña= input("Digite su contraseña: ")
    
print("Bienvenido de vuelta andres")