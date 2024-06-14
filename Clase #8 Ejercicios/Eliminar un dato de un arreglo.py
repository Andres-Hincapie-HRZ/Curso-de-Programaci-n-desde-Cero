# Eliminar un dato especifico de un arreglo
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for fila in matriz:
    if 2 in fila:
        fila.remove(2)
        print(fila)

print(matriz)



