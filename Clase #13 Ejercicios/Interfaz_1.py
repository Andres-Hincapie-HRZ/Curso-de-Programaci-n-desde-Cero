import tkinter as tk
from tkinter import *

def mostrar_texto():
    palabra = entry.get()
    resultado_label.config(text=palabra)

def borrar_texto():
    entry.delete(0,END)
    resultado_label.config(text=" ")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Palabras")

# Configurar el tamaño y el color de fondo de la ventana
ventana.geometry("300x300")
ventana.config(bg='#2C3E50')

# Crear y ubicar los widgets
label = Label(ventana, text="Introduzca la palabra:", bg='#2C3E50', fg='white')
label.pack(pady=10)

entry = Entry(ventana, width=30)
entry.pack(pady=5)

# Crear un marco blanco para mostrar el resultado
resultado_frame = LabelFrame(ventana, text="Resultado", width=250, height=100, bg='white', fg='black', bd=5,relief='sunken')
resultado_frame.pack(pady=5)
resultado_frame.pack_propagate(False)

resultado_label = Label(resultado_frame, text="", bg='white')
resultado_label.pack(expand=True, pady=10, padx=10)

mostrar_btn = Button(ventana, text="Mostrar Texto", command=mostrar_texto)
mostrar_btn.pack(side=LEFT, padx=(50, 10), pady=10)

borrar_btn = Button(ventana, text="Borrar", command=borrar_texto)
borrar_btn.pack(side=RIGHT, padx=(10, 50), pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
