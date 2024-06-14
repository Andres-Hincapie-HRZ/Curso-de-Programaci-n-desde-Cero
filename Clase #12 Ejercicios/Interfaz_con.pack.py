import tkinter as tk
from tkinter import *
# Creación de la interfaz
ventana_pack = tk.Tk()
ventana_pack.title("Interfaz con .pack")
# Color de la interfaz
ventana_pack.config(bg="#283747")
# Tamaño de la interfaz
ventana_pack.geometry("300x300")
    

# Crear botones y ubicarlos con .pack'
boton1 = Button(ventana_pack, text="Botón 1")
boton1.pack(pady=10)

boton2 = Button(ventana_pack, text="Botón 2")
boton2.pack(pady=10)

boton3 = Button(ventana_pack, text="Botón 3")
boton3.pack(pady=10)

boton4 = Button(ventana_pack, text="Botón 4")
boton4.pack(pady=10)

boton5 = Button (ventana_pack, text="clase#12")
boton5.pack(pady=40, padx=10)

# Ejecutar el bucle principal de la ventana
ventana_pack.mainloop()
