curso="Curso"
nombre="php"
result="{a} de {b}".format(a=curso,b=nombre)
print(result.upper())#mayuscula
print(result.lower())#minuscula
print(result.title())#minuscula
print(result.find('p'))#buscar
print(result.count('p'))#cuenta caracter
print(result.replace('p','h'))#remplazo
print(result.split(' '))#corte