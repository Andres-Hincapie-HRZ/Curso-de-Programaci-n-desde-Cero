# Funciones  para cada operacion
def suma(x,y):
    return x + y
def resta(x,y):
    return x - y
def multiplicacion(x,y):
    return x * y
def division(x,y):
    if y != 0:
        return x / y
    else:
        return "Error"

# Función para manejar el botón de igual
def igual():
    try:
        entrada_texto = entrada.get()
        if '+' in entrada_texto:
            x, y = entrada_texto.split('+')
            resultado = suma(int(x), int(y))
        elif '-' in entrada_texto:
            x, y = entrada_texto.split('-')
            resultado = resta(int(x), int(y))
        elif '*' in entrada_texto:
            x, y = entrada_texto.split('*')
            resultado = multiplicacion(float(x), float(y))
        elif '/' in entrada_texto:
            x, y = entrada_texto.split('/')
            resultado = division(float(x), float(y))
        
        entrada.delete(0,END)
        entrada.insert(END, str(resultado))
    except Exception as e:
        entrada.delete(0, END)
        entrada.insert(END, "Error")
        
# Función para manejar la entrada de números y operaciones
def agregar_caracter(caracter):
    entrada.insert(END, caracter)

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, END)

# Función para borrar el último caracter
def borrar():                     
    entrada.delete(len(entrada.get())-1,END)