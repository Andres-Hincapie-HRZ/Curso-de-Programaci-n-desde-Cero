'''Crea un programa que le pregunte al usuario
que telefono desea comprar y su costo,
agregale el iva del 19% más la comisión del
35% y muestra el nombre del producto, su
costo, el costo con el iva y la comisión y el
costo total.
'''
# Solicitar al usuario el nombre del teléfono que desea comprar
nombre_telefono = input("Ingresa el nombre del teléfono que deseas comprar: ")

# Solicitar al usuario el costo del teléfono
costo_telefono = float(input("Ingresa el costo del teléfono: "))

# Calcular el IVA (19%)
iva = costo_telefono * 0.19

# Calcular la comisión (35%)
comision = costo_telefono * 0.35

# Calcular el costo total (costo + IVA + comisión)
costo_total = costo_telefono + iva + comision

# Mostrar los resultados
print("Producto:", nombre_telefono)
print("Costo del teléfono:", costo_telefono)
print("Costo con IVA (19%):", costo_telefono + iva)
print("Costo con IVA y comisión (35%):", costo_total)