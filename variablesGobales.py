"""
def palindromo():
    nuevo_valor=frace.replace(' ','')#variables locales
    return nuevo_valor==frace[::-1]#retorna cadena de ccaracteres alrevez
frace='anita lava la tina '#variable global
resultado=palindromo()
print(resultado)
"""
def valor_gloval():
    global name
    name ="alex"
name="carlos"
print(name)
valor_gloval()
print(name)
#crear variables globales

def create_global():
   global apellido
   apellido="yungan"
create_global()

print(apellido)
