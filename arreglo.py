arreglo = [10,9,8,10,7,10,"Uriel"]

#imprime todo el arreglo
#print "Mi primera calificacion fue " + str(arreglo)

print "Mi primera calificacion fue " + str(arreglo[0])
print "Mi segunda calificacion fue " + str(arreglo[1])
print "Mi primera calificacion fue " + str(arreglo[6])

print ("Modificacion del indice 6 del arreglo: ")
arreglo[6] = 8
print arreglo

print("Extrayendo desde el indice 2 al 5 del arreglo: ")
print arreglo[2:5]

print "Recorriendo el arreglo: "
for x in arreglo:
  print x

print "Numero de elementos que contiene el arreglo: "
print len(arreglo)

print "Otra forma de recorrer el arreglo: "
for i in range(len(arreglo)):
  print arreglo[i]
  print i

arreglo = [10,9,8,10,7,10,9 ]
suma_calificaciones = 0

for i in range(len(arreglo)):
  suma_calificaciones = suma_calificaciones + arreglo[i]
promedio = float(suma_calificaciones) / len(arreglo)
print ("Promedio: ") + str (promedio)

publicaciones = ["Comida en instagram","Se siente entusiasmado por el curso","Estoy aburrido"]
print("Muro de Facebook de Uriel: ")
for publicacion in publicaciones:
  print publicacion