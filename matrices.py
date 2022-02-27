# arreglos de mas de 1 dimension

n = 11

#inicializamos la matriz con 0's
matriz = [ [0 for i in range(n)] for j in range(n)]

#recorriendo la matriz
for i in range(len(matriz)):
  #columnas
  arreglo = matriz[i]
  #filas
  for j in range(len(arreglo)):
    arreglo[j] = i * j
#print matriz
i = 0
j = 0
for i in range(len(matriz)):
  arreglo = matriz[i]
  print arreglo

numero_uno = int(raw_input("Dame el numero uno a multiplicar: "))
numero_dos = int(raw_input("Dame el numero dos a multiplicar: "))

print "El resultado de multiplicar " + str(numero_uno) + " por numero dos " + str(numero_dos) + " es: " + str(matriz[numero_uno][numero_dos])