#con los properties se puede optener el attributo privado
class Usuario:
    def __init__(self,username,password,email):
        self.username=username
        self.__password=self.__generar_password(password)
        self.email=email
    def __generar_password(self,passw):
      return  passw.upper()
    @property#para optener
    def password(self):
        return self.__password
    @password.setter
    def password(self,valor):
        self.__password=self.__generar_password(valor)

user=Usuario('alex','al1da','yungan@hotmail.es')
user.password="ales111"
print(user.password)
