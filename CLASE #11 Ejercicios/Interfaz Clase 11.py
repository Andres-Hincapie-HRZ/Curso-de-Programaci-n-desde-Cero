# Importar libreria tkinter para crear interfaces
import tkinter as tk
# Importar todos los modulos de la libreria tkinter 
from tkinter import *

# Crear la ventana principal
ventana = tk.Tk()

# Personalizar interfaz
ventana.title("Mi primera ventana")
ventana.geometry("400x400")
ventana.iconbitmap("logo.ico")
ventana.config(bg= "yellow")

# Como crear un Frame (Marco)
marco_uno = Frame(ventana)
marco_uno.config(width=300,height=50)
marco_uno.config(bd=5,relief="sunken")
marco_uno.pack(pady=10, padx=0) # Pady --> para espacio en y Padx --> espacio en x

marco_dos= LabelFrame(ventana,text="Resultado marco")
marco_dos.config(width=300,height=50,bd=5,relief="sunken")
marco_dos.pack(pady=10,padx=0)

Etiqueta= Label(marco_dos,text="resultado marco dos")
Etiqueta.place(x=5,y=5)

nuevo_marco=LabelFrame(ventana, text="nuevo marco")
nuevo_marco.config(width=300,height=100)
#nuevo_marco.config(bg="blue")
nuevo_marco.config(bd=5,relief="sunken")
nuevo_marco.pack(pady=10,padx=5)

Etiqueta_nueva= Label(nuevo_marco,text="total:...")
Etiqueta_nueva.place(x=5,y=5)

cuadro_texto= Entry(nuevo_marco,width=20)
cuadro_texto.place(x=150,y=5)
# Iniciar la interfaz
ventana.mainloop()

