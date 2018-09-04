#funciones
def factorial_numero(numero):
    
    factorial=1
    while numero>0:
        factorial=factorial*numero
        numero-=1;
    #print(factorial)
    return factorial
#lista=list(range(1,6))
#print(lista)
for val in range(1,6):
  #print(factorial_numero(val))
  res=factorial_numero(val)
  print(res)