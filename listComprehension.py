#lista = [valor for valor in range(0, 101)]
#lista = [valor for valor in range(0, 101)]
lista = [valor for valor in range(0, 101) if valor % 2==0]
tupla =tuple((valor for valor in range(0, 101) if valor % 2==0))
#crear diccionario
diccionario = {indice:valor for indice,valor in enumerate(lista) if indice<=10}
print(lista)
print(tupla)
print(diccionario)
