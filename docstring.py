#la primera lineaa de una funcion debe ir la documentacion
def generador(*args):
    """ recibe n cantidad de numeros y regresa ademas true o false si el numero es mayor a 5"""
    for valor in args:
        yield valor,True if valor>5 else False
lista=list (generador(1,2,3,4))
print(lista)
name=generador.__name__
print(name)
documentation=generador.__doc__
print(documentation)