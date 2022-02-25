numero_magico = int(raw_input("Dame el numero magico: "))
numero_no_magico = int(raw_input("Adivina el numero magico: "))

while numero_magico != numero_no_magico:
  if numero_magico > numero_no_magico:
    numero_no_magico = int(raw_input("Ups! Fallaste, intenta con un numero mas grande: "))
  """ else: """
    continue
    numero_no_magico = int(raw_input("No adivinaste, intenta con un numero mas bajo: "))

print "Bien hecho, ganaste!!!"