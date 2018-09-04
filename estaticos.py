class Circulo:

    def __init__(self,radio):
        self.radio=radio
    def area(self):#cuando tiene self metodos de instalcia
        return self.radio*self.radio*self.pi()
    @staticmethod#ejemplo de metodo estatico
    def pi():
        return 3.14 
uno=Circulo(12)
print(uno.pi())
print(uno.area())