#las clases siempre van en mayuscula y nada de gion bajo
#LapizGrande
class Lapiz:
    def __init__(self,color='blue',borrador=False,grafito=False):#es como el constructor
        self.color=color
        self.contiene_borrador=borrador
        self.usa_grafito=grafito
    #metodos
    def dibujar(self):
        print('esta dibujando')
    def borrar(self):
        if self.puede_borrador():
            print('el lapiz esta borrando')
        else:
            print('no se puede borrar')
    def puede_borrador(self):
        #print(self.contiene_borrador)
        return self.contiene_borrador
#este es un lapiz
mi_lapiz=Lapiz()#ya q en el constructor esta valores por defecto
#mi_lapiz=Lapiz('yellow',True,True)#pasar parametros en el constructor
#mi_lapiz.color='blue'
#print(mi_lapiz.color)
#mi_lapiz.dibujar()
mi_lapiz.borrar()
