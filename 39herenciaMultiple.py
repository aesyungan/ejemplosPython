#no s epuede heredar metodos privados
class Mascota:
    nombre='no se'
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
    def gato_cazador(self):
        self.cazar()
class Jaguar(Felino):
    pass
gato=Gato()
jaguar=Jaguar()

print(gato.nombre)