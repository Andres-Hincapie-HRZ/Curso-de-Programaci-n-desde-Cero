# Importar libreria tkinter para crear interfaces
import tkinter as tk
# Importar todos los modulos de la libreria tkinter 
from tkinter import *

# Crear la ventana principal
ventana = tk.Tk()

# Personalizar interfaz
ventana.title("Mi primera ventana")
ventana.geometry("400x100")
ventana.iconbitmap("logo.ico")
ventana.config(bg= "yellow")

# Como crear un Frame (Marco)
marco_uno = Frame(ventana)
marco_uno.config(width=300,height=50)
marco_uno.pack(pady=10, padx=0) # Pady --> para espacio en y Padx --> espacio en x

# Iniciar la interfaz
ventana.mainloop()

