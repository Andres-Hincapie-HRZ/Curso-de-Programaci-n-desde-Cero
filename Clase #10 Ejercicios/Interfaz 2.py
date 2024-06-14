import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Personalizar interfaz
ventana.title("Mi primera ventana")
ventana.geometry("400x100")
ventana.iconbitmap("logo1.ico")
ventana.config(bg="#4B0547")
ventana.resizable(0,1)

# Iniciar la interfaz
ventana.mainloop()

