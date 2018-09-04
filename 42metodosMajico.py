class Usuario:
    def __new__(cls):#este es el constructor #primero se ejecuta el new
        print("metodo1")
        return super().__new__(cls)#ºdebe retornar#luego se ejecuta el init
    def __init__(self):
        print("metodo2")
    def __str__(self):
        return "muestra cunado imprime y ya no muestra referencia de memoria"
    def __getattr__(self,nombre):
        print("aqui mostramos q no se encontro el attributo")

usuario=Usuario()

print(usuario) #ejemplo str
print(usuario.noatributo) #ejemplo getattr