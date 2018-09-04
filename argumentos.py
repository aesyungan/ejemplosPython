#n contidad de argumentos
#normalmente se usan *args para decir q va mandar n cantidad de argiumentos 
def suma (*val):#todo lo q pasa se convierte en tupla los parametros
    r=0
    for v in val:
        r+=v
    return r
res=suma(2,1)
print(res)
#otro ejemplo
#n valores con ** usa diccionarios
def suma2 (**kwargs):
   print(kwargs)
   return kwargs
res=suma2(a='ales',nombre="carlos")
print(res)
#sabe de q tipo es  algo
value =12
print(type(value))