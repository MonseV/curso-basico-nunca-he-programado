numero = int(raw_input("Dame el numero de la tabla de multiplicar "))

for x in range(0,11):
  print str(numero) + " * " + str(x) + " = " + str((numero * x))