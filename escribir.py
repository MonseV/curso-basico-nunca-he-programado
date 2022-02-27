# w -> permisos de escritura
# a -> lo que se escribe se va al final del archivo

n = 10
matriz = [ [0 for i in range(n)] for j in range(n)]

for i in range(len(matriz)):
  #columnas
  arreglo = matriz[i]
  #filas
  for j in range(len(arreglo)):
    arreglo[j] = i * j

archivo = open('ejemplo.txt','w')

for i in range(len(matriz)):
  arreglo = matriz[i]
  #recorrido indice por indice
  for j in range(len(arreglo)):
    numero = arreglo[j]
    #si j es mayor que el tamano del arreglo menos 1
    if j < (len(arreglo) - 1):
      archivo.write(str(numero)+",")
    #aqui entra el ultimo valor
    else:
      archivo.write(str(numero))
  if i < (len(matriz) - 1):
    archivo.write("\n")