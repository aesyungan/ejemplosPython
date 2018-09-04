fruta="kiwii"

if fruta=='kiwi':
    print("es kiwi")
elif fruta=='manzana':
  print("es manzana")
else:
    print("no es kiwi")

mesage='el valor es kiwi' if fruta=='kiwi' else 'no es kiwi'
print(mesage)
#pass es para saltar errores
# 
# todos los valores vacios o no declarados son falsos
# [], (), {} ,0, ''
# None
valor =2#poner a una variable que no tiene valor
valor2=6
print(valor)  
#valor=None
if valor and valor2==6:
    print("existe valor")
else:
    print("no existe valor")
valor=None
if valor or valor2==6:
    print("existe valor")
else:
    print("no existe valor")