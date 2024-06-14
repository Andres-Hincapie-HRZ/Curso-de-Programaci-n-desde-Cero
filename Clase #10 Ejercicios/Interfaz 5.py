import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Personalizar interfaz
ventana.title("Mi primera ventana")
ventana.geometry("400x100")
ventana.iconbitmap("logo.ico")
ventana.config(bg= "yellow")
ventana.resizable(1,0)

'''
ventana.resizable(0,0) # no escalable 
ventana.resizable(1,0) # solo el ancho 
ventana.resizable(0,1) # solo el alto 
ventana.resizable(1,1) # escalable
'''
# Iniciar la interfaz
ventana.mainloop()

