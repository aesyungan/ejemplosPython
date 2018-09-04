#no s epuede heredar metodos privados
class Mascota:
    def __init__(self,nombre):
        self.nombre=nombre
    def mostrar_nombre(self):
        print("se llama:",self.nombre)
class Animal:
    @property
    def terrestre(self):
        return True
class Felino(Animal,Mascota):# clase padre
    @property
    def garras_retractiles(self):
        return True;
    def cazar(self):
        print("el felino esta cazando")
class Gato(Felino):
    def __init__(self,nombre):
        Mascota.__init__(self,nombre)
        self.nombre_gato=nombre
    def gato_cazador(self):
        self.cazar()
    def mostrar_nombre(self):#override
        Mascota.mostrar_nombre(self)
        print("nombre de gato es :",self.nombre)
class Jaguar(Felino):
    pass
gato=Gato('Michu')
#jaguar=Jaguar()

gato.mostrar_nombre()