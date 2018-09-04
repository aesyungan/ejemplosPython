#variables en una clase
class Circulo:
    pi=3.1416#variable de clase no se ncesita crear un objeto para ver ese dato
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        return self.radio*self.radio*self.pi

uno=Circulo(10)
dos=Circulo(5)
print(uno.radio)
print(dos.radio)
print(Circulo.pi)#variable de clase no es necesario instanciar
#sabr atributos de la clase menos las variables de la clase
#print(Circulo.__dict__)
print(uno.area())