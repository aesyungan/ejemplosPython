import random

val =random.randint(0,20)
print(val)
#en lista
lista=[True,"hola",23,10.21]
val =random.choice(lista)
print(val)
#desordenar lista
random.shuffle(lista)
print(lista)
