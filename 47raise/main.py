class TinyIntError(Exception):
    def __init__(self):
        self.message="El número no cuenta con las caracteristicas de un numero tinyInt"
    def __str__(self):
        return self.message
def validate_tiny_int(val):
    return val>=0 and val<=255
def validate_val(val):
    try:
     return isinstance(int(val),int)
    except ValueError as error:
        return False
def tiny_int(val):
    try:
        if validate_val(val) and validate_tiny_int(val):
            return True
        else:
            raise TinyIntError()
    except TinyIntError as error:
        print(error)
"""
def call_back_function():
    print("esto se ejecuta cuando hay error")"""
print(tiny_int(1155))