import tkinter as tk
from tkinter import *

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Llamada")
ventana.geometry("300x400")
ventana.configure(bg='#212F3C')

# Etiqueta para mostrar los números marcados
etiqueta_numeros_marcados = Label(ventana, text="", font=("Arial", 12), bg='white', width=30, height=2)
etiqueta_numeros_marcados.pack(pady=10)

# Campo de entrada para mostrar el número marcado
entrada_numero = Entry(ventana, font=("Arial", 14), width=15, justify='center')
entrada_numero.pack(pady=10)

# Marco para los botones numéricos
botones_frame = Frame(ventana)
botones_frame.pack(pady=10)

# Botones del 1 al 9
numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["", 0, ""]
]

for r, fila in enumerate(numeros):
    for c, num in enumerate(fila):
        if num != "":
            boton = Button(botones_frame, text=str(num), width=5, height=2)
            boton.grid(row=r, column=c, padx=5, pady=5)

# Botón de borrar
boton_borrar = Button(ventana, text="Borrar", width=10, height=2)
boton_borrar.pack(side=tk.LEFT, padx=20, pady=20)

# Botón de llamar
boton_llamar = Button(ventana, text="Llamar", width=10, height=2)
boton_llamar.pack(side=tk.RIGHT, padx=20, pady=20)

# Ejecutar la aplicación
ventana.mainloop()
