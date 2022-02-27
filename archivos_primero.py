# r -> permisos de lectura

archivo = open("ejemplo.txt","r")
matriz = []
for linea in archivo:
  #agregandolo al arreglo
  arreglo_con_cadenas = linea.split(",")
  arreglo = []
  for j in range(len(arreglo_con_cadenas)):
    #el int es para quitar los saltos de lineas y dejar los numeros enteros
    numero_sin_caracteres = int(arreglo_con_cadenas[j])
    arreglo.append(numero_sin_caracteres)
    #para formar la matriz
    matriz.append(arreglo)

numero_uno = int(raw_input("Dame el numero uno a multiplicar: "))
numero_dos = int(raw_input("Dame el numero dos a multiplicar: "))

print "El resultado de multiplicar " + str(numero_uno) + " por numero dos " + str(numero_dos) + " es: " + str(matriz[numero_uno][numero_dos])