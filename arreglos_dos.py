frutas = ["Manzana","Mango","Uva","Sandia"]

#Agrega un elemento al arreglo
frutas.append("Fresa")

#Recibe la posicion y el elemento que se agregara al arreglo
""" frutas.insert(3,"Naranja") """
frutas.insert(0,"Naranja")

lenguajes_prog = ["python","javascript","java"]

# Agrega los elementos del arreglo especificados
# al final del arreglo actual.
""" frutas.extend(lenguajes_prog)
print frutas """
""" lenguajes_prog.extend(frutas)
print lenguajes_prog """

#Elimina el elemento del arreglo
""" frutas.remove("Fresa") """

#Elimina el elemento dada una posicion
frutas.pop(3)

print frutas