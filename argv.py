#recibir argumentos al ejecutar un script
import sys
#el primer argumento simpre es el nombre del archivo
if __name__=='__main__':
    if len(sys.argv)==1:
        print("es necesario por lo menos un argumento")
    print(sys.argv)