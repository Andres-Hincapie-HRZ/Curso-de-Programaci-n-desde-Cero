import tkinter as tk

# Creación de la interfaz
ventana_place = tk.Tk()
ventana_place.title("Interfaz con .place")
# Color de la interfaz
ventana_place.config(bg="#283747")
# Tamaño de la interfaz
ventana_place.geometry("300x300")

# Crear botones y ubicarlos de manera desordenada con .place
boton1 = tk.Button(ventana_place, text="Botón 1")
boton1.place(x=20, y=150)

boton2 = tk.Button(ventana_place, text="Botón 2")
boton2.place(x=180, y=30)

boton3 = tk.Button(ventana_place, text="Botón 3")
boton3.place(x=100, y=200)

boton4 = tk.Button(ventana_place, text="Botón 4")
boton4.place(x=250, y=100)

# Ejecutar el bucle principal de la ventana
ventana_place.mainloop()
