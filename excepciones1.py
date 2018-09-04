try:
    print(1/0)
except ZeroDivisionError as ex:
    print("error->",ex) 
#otro error   
try:
    lista=[1,2]
    print(lista[10])
except IndexError as ex:
    print("error->",ex)    
print("se termino el script")
#cuando no sabes q errror va ser
try:
    lista=[1,2]
    print(lista[10])
except Exception as ex:
    print("error->",ex) 
finally:
    print("ejecura al finalizar el bloque try")   
print("se termino el script")
