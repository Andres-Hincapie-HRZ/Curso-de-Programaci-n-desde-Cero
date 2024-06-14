import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Creación de interfaz
ventana = tk.Tk()
ventana.title("Ventana con Botón")
# Color de interfaz
ventana.config(bg="#212F3C")
# Tamaño de interfaz
ventana.geometry("300x500")

# Marco uno
marco_uno = LabelFrame(ventana, text="marco uno")
# Tamaño del marco
marco_uno.config(width=200, height=100)
# Relieve del marco
marco_uno.config(bd=5, relief="sunken")
marco_uno.pack(pady=10)

# Función para la pregunta sí o no
def pregunta_si_no():
    messagebox.askquestion(message="¿Eres programador?", title="Ventana sí o no")

# Función para reintentar
def reintentar():
    return messagebox.askretrycancel("Reintentar", "¿Desea reintentar?")

# Función para sí, no o cancelar
def si_no_cancelar():
    resultado = messagebox.askyesnocancel("Confirmar", "¿Desea continuar?")
    return resultado

# Función para aceptar o cancelar
def aceptar_cancelar():
    messagebox.askokcancel(message="Confirmar", title="¿Desea continuar?")

# Botón para pregunta sí o no
boton_si_no = Button(ventana, text="Pregunta Sí o No", command=pregunta_si_no)
boton_si_no.pack(pady=5)

# Botón para reintentar
boton_reintentar = Button(ventana, text="Reintentar", command=reintentar)
boton_reintentar.pack(pady=5)

# Botón para sí, no o cancelar
boton_si_no_cancelar = Button(ventana, text="Sí, No o Cancelar", command=si_no_cancelar)
boton_si_no_cancelar.pack(pady=5)

# Botón para aceptar o cancelar
boton_aceptar_cancelar = Button(ventana, text="Aceptar o Cancelar", command=aceptar_cancelar)
boton_aceptar_cancelar.pack(pady=5)

ventana.mainloop()
