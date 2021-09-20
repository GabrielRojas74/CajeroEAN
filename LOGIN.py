usuarios=[["gabriel",1234,"restaurante",10_000_000],["ivan",1213,"banco",1000]]
c=0
while True:
    if(c==1):
      break
    opcion=int(input("Digite 1: login, 2:registro: "))
    if(opcion==1):
        usuario=input("Digite usuario: ")#txt
        contraseña=int(input("digite la contraseña: "))#txt
        for i in usuarios:
            if(i[0]==usuario and i[1]==contraseña):
                opciones=int(input("1.consultar saldo, 2.tranferir, 3.retirar:  "))
                if(opciones==1):
                    print("tu saldo es: ",i[3])
                elif(opciones==2):
                    destino=input("digite el destino de la transferencia: ")
                    for x in usuarios:
                       if(x[0]==destino):
                           dinero_trasferir=int(input("Digite dinero a tranferir:"))
                           i[3]=i[3]-dinero_trasferir
                           x[3]=x[3]+dinero_trasferir
                           print("Transferencia exitosa")
                           print("Su nuevo saldo es: ", i[3])   
                break
    else:
        username=input("Digite usuario: ")#txt
        contraseña=int(input(("Digite la contraseña: "))#txt
        tipo=input("tipo: ")
        monto=int(input("Digite monto: "))
        usuario=[]
        usuario.append(username)
        usuario.append(contraseña)
        usuario.append(tipo)
        usuario.append(monto)
        usuario.append(usuario)
        print("Ha sido resgistrado")
        print(usuarios)
        
#si se puede
