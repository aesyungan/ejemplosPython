def suma(val1,val2):
    return val1+val2
 
def divicion(val1,val2):
    return val1/val2
def multiplicacion(val1,val2=1):#inicializa un valor por defecto si no pasa por parametro
    return val1*val2
def multiple_valores():
    #retornar mulpiples valores
    return "Sreing",True,12#osea retorna una tupla
#res=suma(1,4) 
#res=divicion(10,2) #forma1
#res=multiplicacion(val2=2,val1=10)#forma2 
res=multiple_valores()
string, booleano,entero=res;#optener multiples valores
#otra forma
#string=res[0]
#print(string)
#asignar  funciones a variables
mi_variable=multiplicacion
res=mi_variable(1,19)#ejecutar la funcion q tiene asignado la funcion
print(res)

#funcion sobre otra funcion
def mostrar_resultado(function):
    print(function(6,8))
mostrar_resultado(mi_variable)