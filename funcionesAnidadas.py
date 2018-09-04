#funciones dentro de otra
"""
def division(n1,n2):
    def validacion(n1,n2):
        return n1>0 and n2>0
    if validacion(n1,n2):
        return n1/n2 
res=division(2,2)
print(res)
"""
#funcion closure funciones q crean funcones

def crear_funcion(n1,n2):
    def validacion():
        print("se ejecuta validacion")
        return n1>0 and n2>0
    return validacion
res=crear_funcion(1,2)
print(res())

def aplicar_funcion(func):
    func()
nueva_f=crear_funcion(1,2)
aplicar_funcion(nueva_f)