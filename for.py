# lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in lista:
    print(val)
# tupla
lista2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for val in lista2:
    print(val)
# genera valores en un rango
# nuevo_rango=range(10) #de 0 a 10
# nuevo_rango=range(0,10,2) #de 0 a 10 saltando osea de 2 en 2
nuevo_rango = range(0, 10)
for val in nuevo_rango:
    print(val)
# optener indice
# indice=0
# devuelve una tupla con indice y el valor
for indice, val in enumerate(lista):
    print("indice", indice, "valor", val)
#recorer dede un indice hasta otro
#len optiene el tamaño de la lista 
print(len(lista))
for val in range(0,len(lista)):
    print(val)
#diccionario
diccionario={'a':10,10:8080}
for llave,valor in diccionario.items():
    print("llave:",llave,"valor",valor)