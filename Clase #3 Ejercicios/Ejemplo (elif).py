'''Imagina que estás en una tienda de helados y estás tratando de decidir qué sabor quieres.
El Heladero te ofrece varias opciones y tú tienes ciertos criterios en mente.
El if sería como tu primera opción. Digamos que quieres chocolate. Entonces, dices
"Si tienen chocolate, quiero un cono de chocolate".

Pero luego el heladero te dice que lamentablemente se les acabó el chocolate. 
Ahora, tienes que pensar en una segunda opción. Aquí es donde entra en juego el elif.

Entonces, miras las otras opciones disponibles. Y te gusta la vainilla, dices 
"¡De acuerdo, si no hay chocolate, quiero un cono de vainilla!".

El elif es como tener una segunda opción preparada en caso de que tu primera opción no esté disponible.
Es una forma de decir "si no se cumple la primera condición, entonces intentemos con esta otra".
'''

sabor_disponible = "vainilla"

if sabor_disponible == "chocolate":
    print("¡Quiero un cono de chocolate!")
elif sabor_disponible == "vainilla":
    print("Bueno, en ese caso, quiero un cono de vainilla.")
else:
    print("Oh, entonces no quiero helado.")