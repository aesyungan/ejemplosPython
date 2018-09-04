from calculadora import __name__ as cal
print(__name__)
print(cal)
#como sabel si es el script es principal
#simpre tendra __main__ el script q se ejecuta
if __name__ =='__main__':
    print('modulo principal')