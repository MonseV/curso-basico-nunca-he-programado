#recursividad es una funcion que se llama asi misma

#importamos la funcion factorial desde la libreria math
from math import factorial

""" def my_factorial(n):
  factorial_total = 1
  while n > 1:
    #factorial_total *= n
    factorial_total = factorial_total * n
    #n -= 1
    n = n - 1
  return factorial_total """

#funcion de python
print factorial(6)

#Asi se saca el factorial
""" print "Factorial de 5: "
print(5*4*3*2*1) """
""" print "Factorial de 6: "
print(6*5*4*3*2*1) """

# PRIMERA ITERACION
# n = 6
# factorial_total = 1

# n > 1 = 6 > 1 si, entonces
# factorial_total = 1 * n = 1 * 6 = 6
# n - 1 = 6 - 1 = 5

# SEGUNDA ITERACION
# n = 5
# factorial_total = 6

# 5 > 1 si, entonces
# factorial_total = 6 * 5 = 30
# 5 - 1 = 4

# TERCERA ITERACION
# n = 4
# factorial_total = 30

# funcion my_factorial
""" print my_factorial(6) """

# FUNCION RECURSIVA
def my_factorial(n):
  factorial_total = 1
  if n > 1:
    return n * my_factorial(n - 1)
  """ else:
    return 1 """
  return 1

print my_factorial(6)