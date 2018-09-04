lista=["hola","que ","hace",14,True]
lista.append("end");#agrega al final
lista.insert(0,"init");#puede poner en el indice q quiera
#lista.remove(14);#eliminar 
print(lista)
print(lista.pop())#
lista=[5,4,2]
print(lista.sort())#orden acedente
#unir
lista2=[9,6]
lista.extend(lista2)
print(lista)
lista.append(lista2)
print(lista)