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
marco_uno= Frame(ventana)
marco_uno.config(width=400,height=100)
marco_uno.config(bg="blue")
marco_uno.pack(pady=0,padx=0)

# Iniciar la interfaz
ventana.mainloop()

