#no s epuede heredar metodos privados
class Animal:
    @property
    def terrestre(self):
        return True
class Felino(Animal):# clase padre
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
print(gato.garras_retractiles)
print(gato.gato_cazador())
print(jaguar.garras_retractiles)
print(jaguar.terrestre)