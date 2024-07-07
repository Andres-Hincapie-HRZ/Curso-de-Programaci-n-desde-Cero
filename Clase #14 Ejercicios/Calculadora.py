#import tkinter as tk
import tkinter as tk
from tkinter import *
# Funciones para cada operación
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
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
            resultado = multiplicacion(int(x), int(y))
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

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("CALCULADORA")

# Configuración del campo de entrada
entrada = tk.Entry(ventana, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entrada.grid(row=0, column=0, columnspan=4)
#
# Configuración de los botones
boton_config = {
    "width": 5,
    "height": 2,
    "bg": "#444444",
    "fg": "white",
    "font": ("Arial", 18),
    "borderwidth": 0
}

# Crear botones uno por uno
boton_parentesis_izquierdo = tk.Button(ventana, text='(', **boton_config, command=lambda: agregar_caracter('('))
boton_parentesis_izquierdo.grid(row=1, column=0, padx=5, pady=5)

boton_parentesis_derecho = tk.Button(ventana, text=')', **boton_config, command=lambda: agregar_caracter(')'))
boton_parentesis_derecho.grid(row=1, column=1, padx=5, pady=5)

boton_clear = tk.Button(ventana, text='C', **boton_config, command=limpiar)
boton_clear.grid(row=1, column=2, padx=5, pady=5)

boton_borrar = Button(ventana, text='←', **boton_config, command=borrar)
boton_borrar.grid(row=1, column=3, padx=5, pady=5)

boton_7 = tk.Button(ventana, text='7', **boton_config, command=lambda: agregar_caracter('7'))
boton_7.grid(row=2, column=0, padx=5, pady=5)

boton_8 = tk.Button(ventana, text='8', **boton_config, command=lambda: agregar_caracter('8'))
boton_8.grid(row=2, column=1, padx=5, pady=5)

boton_9 = tk.Button(ventana, text='9', **boton_config, command=lambda: agregar_caracter('9'))
boton_9.grid(row=2, column=2, padx=5, pady=5)

boton_suma = tk.Button(ventana, text='+', **boton_config, command=lambda: agregar_caracter('+'))
boton_suma.grid(row=2, column=3, padx=5, pady=5)

boton_4 = tk.Button(ventana, text='4', **boton_config, command=lambda: agregar_caracter('4'))
boton_4.grid(row=3, column=0, padx=5, pady=5)

boton_5 = tk.Button(ventana, text='5', **boton_config, command=lambda: agregar_caracter('5'))
boton_5.grid(row=3, column=1, padx=5, pady=5)

boton_6 = tk.Button(ventana, text='6', **boton_config, command=lambda: agregar_caracter('6'))
boton_6.grid(row=3, column=2, padx=5, pady=5)

boton_resta = tk.Button(ventana, text='-', **boton_config, command=lambda: agregar_caracter('-'))
boton_resta.grid(row=3, column=3, padx=5, pady=5)

boton_1 = tk.Button(ventana, text='1', **boton_config, command=lambda: agregar_caracter('1'))
boton_1.grid(row=4, column=0, padx=5, pady=5)

boton_2 = tk.Button(ventana, text='2', **boton_config, command=lambda: agregar_caracter('2'))
boton_2.grid(row=4, column=1, padx=5, pady=5)

boton_3 = tk.Button(ventana, text='3', **boton_config, command=lambda: agregar_caracter('3'))
boton_3.grid(row=4, column=2, padx=5, pady=5)

boton_multiplicacion = tk.Button(ventana, text='*', **boton_config, command=lambda: agregar_caracter('*'))
boton_multiplicacion.grid(row=4, column=3, padx=5, pady=5)

boton_0 = tk.Button(ventana, text='0', **boton_config, command=lambda: agregar_caracter('0'))
boton_0.grid(row=5, column=0, padx=5, pady=5)

boton_punto = tk.Button(ventana, text='.', **boton_config, command=lambda: agregar_caracter('.'))
boton_punto.grid(row=5, column=1, padx=5, pady=5)

boton_igual = tk.Button(ventana, text='=', **boton_config, command=igual)
boton_igual.grid(row=5, column=2, padx=5, pady=5)

boton_division = tk.Button(ventana, text='/', **boton_config, command=lambda: agregar_caracter('/'))
boton_division.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()
