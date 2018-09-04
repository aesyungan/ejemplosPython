class Usuario:
    def __init__(self):
        self.__password="es un password"

usuario=Usuario()
usuario.nombre="alex"#no esta creado el attributo en la clase pro al poner asi se crea un attributo  publico
usuario.__password="ya no es secreto"
print(usuario.nombre)
print(usuario.__dict__)