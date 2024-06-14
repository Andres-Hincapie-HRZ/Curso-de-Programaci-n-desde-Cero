import tkinter as tk
from tkinter import *

def sumar():
    numero1 = entrada_numero1.get()
    numero2 = entrada_numero2.get()

    resultado = float(numero1) + float(numero2)
    resultado_label.config(text=str(resultado))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Suma de Dos Números")

# Configuración del color de fondo de la ventana
ventana.configure(bg='#2C3E50')

# Etiqueta para el primer número
etiqueta_numero1 = Label(ventana, text="Número 1:", bg='#2C3E50', fg='white')
etiqueta_numero1.grid(row=0, column=0, padx=10, pady=10)

# Entrada de texto para el primer número
entrada_numero1 = Entry(ventana, width=30)
entrada_numero1.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta para el segundo número
etiqueta_numero2 = Label(ventana, text="Número 2:", bg='#2C3E50', fg='white')
etiqueta_numero2.grid(row=1, column=0, padx=10, pady=10)

# Entrada de texto para el segundo número
entrada_numero2 = Entry(ventana, width=30)
entrada_numero2.grid(row=1, column=1, padx=10, pady=10)

# Marco para mostrar el resultado
marco_resultado = Frame(ventana, bg='white', bd=2, relief="sunken")
marco_resultado.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# Etiqueta para mostrar el resultado dentro del marco
resultado_label = Label(marco_resultado, text="", bg='white', fg='black', width=28, height=5)
resultado_label.pack(padx=10, pady=10)

# Botón para sumar los números
boton_sumar = Button(ventana, text="Sumar", command=sumar)
boton_sumar.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

# Ajuste del tamaño de la ventana para que se vea correctamente
ventana.geometry('300x300')

# Ejecutar la aplicación
ventana.mainloop()
