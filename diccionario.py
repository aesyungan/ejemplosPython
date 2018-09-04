# las claves son inmutables
#llave :valor
diccionario = {'a': 55, 'edad': 22, (1, 1): False}
# si las llaves son iguales toma el ultim valor
# añadiir mas valores
diccionario[12] = "hola q hace"
# modificar
diccionario['edad'] = "no se"
#optener
valor = diccionario['edad']
#si no hay en el diccionario manda se puede mandar cualquier otro tipo
valor = diccionario.get('nombre',"no existe en el diccionario")
#eliminar
del diccionario['edad']
#print(diccionario)
#print(valor)
#optener llaves
llaves=diccionario.keys()
#optener llaves como listas
print(llaves)
llaves=list (diccionario.keys())
print(llaves)
#optener valores
valores=diccionario.values()
print(valores)
#lista
valores=list(diccionario.values())
print(valores)
#tuplas
valores=tuple(diccionario.values())
print(valores)
#inir diccionarios
diccionario2={221:'diccionariio 2'}
diccionario.update(diccionario2)
print(diccionario)