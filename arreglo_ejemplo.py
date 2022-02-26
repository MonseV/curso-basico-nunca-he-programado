#Pedir las calificaciones
#Guardarlas en un arreglo
#Recorrer ese arreglo y sumar las calificaciones
#,luego divido la suma entre el total de calificaciones

calificacion = 0

calificaciones = []
i = 1

print "Para salir coloca un numero negativo"
while calificacion >= 0:
  calificacion = int(raw_input("Dame la calificacion " + str(i) + ":"))
  if calificacion >= 0:
    calificaciones.append(calificacion)
  i = i + 1

  suma = 0

for cal in calificaciones:
  suma = suma + cal

print "Tu promedio es: " + str(suma/len(calificaciones))