# Importar librerias y modulos
import tkinter as tk
from tkinter import *
# Configuracin de la interfaz grfica
ventana = tk.Tk()
ventana.title("Calculadora")

# Configuracin del campo de entrada
entrada = Entry(ventana, width=16, font=('Arial', 24), bd=2, relief='solid')
entrada.grid(row=0, column=0, columnspan=4)

# Configuracin de los botones
boton_config = {
        "width": 5,
        "height": 2,
        "bg": "#444444",
        "fg": "white",
        "font": ("Arial", 18),
        "borderwidth": 0
}

# Crear botones uno por uno
boton_parentesis_izquierdo = Button(ventana, text='(', **boton_config)
boton_parentesis_izquierdo.grid(row=1, column=0, padx=5, pady=5)

boton_parentesis_derecho = Button(ventana, text=')', **boton_config)
boton_parentesis_derecho.grid(row=1, column=1, padx=5, pady=5)

boton_clear = Button(ventana, text='C', **boton_config)
boton_clear.grid(row=1, column=2, padx=5, pady=5)

boton_borrar = Button(ventana, text='←', **boton_config)
boton_borrar.grid(row=1, column=3, padx=5, pady=5)

boton_7 = Button(ventana, text='7', **boton_config)
boton_7.grid(row=2, column=0, padx=5, pady=5)

boton_8 = Button(ventana, text='8', **boton_config)
boton_8.grid(row=2, column=1, padx=5, pady=5)

boton_9 = Button(ventana, text='9', **boton_config)
boton_9.grid(row=2, column=2, padx=5, pady=5)

boton_suma = Button(ventana, text='+', **boton_config)
boton_suma.grid(row=2, column=3, padx=5, pady=5)

boton_4 = Button(ventana, text='4', **boton_config)
boton_4.grid(row=3, column=0, padx=5, pady=5)

boton_5 = Button(ventana, text='5', **boton_config)
boton_5.grid(row=3, column=1, padx=5, pady=5)

boton_6 = Button(ventana, text='6', **boton_config)
boton_6.grid(row=3, column=2, padx=5, pady=5)

boton_resta = Button(ventana, text='-', **boton_config)
boton_resta.grid(row=3, column=3, padx=5, pady=5)

boton_1 = Button(ventana, text='1', **boton_config)
boton_1.grid(row=4, column=0, padx=5, pady=5)

boton_2 = Button(ventana, text='2', **boton_config)
boton_2.grid(row=4, column=1, padx=5, pady=5)

boton_3 = Button(ventana, text='3', **boton_config)
boton_3.grid(row=4, column=2, padx=5, pady=5)

boton_multiplicacion = Button(ventana, text='*', **boton_config)
boton_multiplicacion.grid(row=4, column=3, padx=5, pady=5)

boton_0 = Button(ventana, text='0', **boton_config)
boton_0.grid(row=5, column=0, padx=5, pady=5)

boton_punto = Button(ventana, text='.', **boton_config)
boton_punto.grid(row=5, column=1, padx=5, pady=5)

boton_igual = Button(ventana, text='=', **boton_config)
boton_igual.grid(row=5, column=2, padx=5, pady=5)

boton_division = Button(ventana, text='/', **boton_config)
boton_division.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()

