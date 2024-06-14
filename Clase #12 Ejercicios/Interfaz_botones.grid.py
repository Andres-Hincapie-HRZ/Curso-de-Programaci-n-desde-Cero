import tkinter as tk
from tkinter import *


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz")
ventana.geometry("220x100")
ventana.config(bg="#283747")

    
# Crear botones
boton1 = Button(ventana, text="Botón 1")
boton1.grid(row=0, column=0, padx=10, pady=10)

boton2 = Button(ventana, text="Botón 2")
boton2.grid(row=0, column=1, padx=10, pady=10)

boton3 = Button(ventana, text="Botón 3")
boton3.grid(row=0, column=2, padx=10, pady=10)

boton4 = Button(ventana, text="Botón 4")
boton4.grid(row=1, column=0, padx=10, pady=10)

boton5 = Button(ventana, text="Botón 5")
boton5.grid(row=1, column=1, padx=10, pady=10)

boton6 = Button(ventana, text="Botón 6")
boton6.grid(row=1, column=2, padx=10, pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
