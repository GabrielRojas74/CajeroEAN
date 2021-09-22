dinero=500000
usuario=str(input("Ingrese su usuario: "))
contraseña=int(input("Ingrese su contraseña: "))
print("Bienvenido ",usuario)
opcion=int(input(("¿Qué desea hacer? Presione 1 para consultar su saldo, Presione 2 para retirar o Presione 3 para transferir dinero a otra cuenta : ")))
if (opcion==1):
    print("Su saldo es de ",dinero)
    print("Gracias por usar y confiar en cajeroEAN=)")
elif (opcion==2):
    retiro=int(input("¿Cuánto desea retirar?: "))
    if (retiro<=dinero):
        print("Se han retirado: ",retiro)
        dinero=dinero-retiro
        print("El sueldo restante en su cuenta es de: ",dinero)
    else:
        print("Usted no posee tal cantidad de dinero=(")
    print("Gracias por usar y confiar en cajeroEAN=)")
elif (opcion==3):
    cuenta=int(input("¿A qué numero de cuenta desea trasferir el dinero?: "))
    transferencia=int(input("¿Cuánto dinero desea transferir a esta cuenta?: "))
    if (transferencia<=dinero):
        print("Se han transferido ",transferencia," a la cuenta ",cuenta)
        print("El dinero restante en su cuenta es de: ",dinero-transferencia)
    else:
        print("Usted no posee tal cantidad de dinero para transferir desde su cuenta=(")
    print("Gracias por usar y confiar en cajeroEAN=)")     
   

