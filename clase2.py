#__attiburo privado utilizar __
class Usuario:
    def __init__(self,username,password,email):
        self.username=username
        self.__password=self.__generar_password(password)
        self.email=email
    def __generar_password(self,passw):
      return  passw.upper()
    def get_pass(self):
        return self.__password
user=Usuario('alex','al1da','yungan@hotmail.es')
print(user.username)
print(user.get_pass())
print(user.email)