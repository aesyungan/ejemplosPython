count=0
while count<=10:
    print("n %s"%(count))
    count+=1
    if count==5:
        print("es numero 5")
        continue #continua el ciclo
    if count==6:
        print("es numero 6")
        break #termina el ciclo y no sale el else de terminado
else:
    print("a terminado")