import sys
import time

#ejemplo barra de progreso
for i in range(100):
    time.sleep(0.5)
    sys.stdout.write("\r%d %%" %i)#imprime i en la misma posicion del terminal
    sys.stdout.flush()