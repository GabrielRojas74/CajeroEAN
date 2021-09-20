# solo se puede consultar el dinero que hay en la caja y retirarlo para darle las vueltas al cliente. se necesita tener un inventario de los billetes y monedas que hay en la caja.
dinero_de_caja=2_456_850


opcion=int(input(("¿Qué desea hacer? Presione 1 para consultar el dinero de la caja, 2 para dar las vueltas al cliente ")))
if (opcion==1):
        print("El dinero en la caja es de: ",dinero_de_caja)
        if (dinero_de_caja>=100_000):
            queda=dinero_de_caja//100_000
            print(str(queda)+ "billete\s de 100_000 pesos")
            dinero_de_caja= dinero_de_caja % 100_000
        if (dinero_de_caja>=50_000):
            queda=dinero_de_caja//50_000
            print(str(queda)+ "billete\s de 50_000 pesos")
            dinero_de_caja= dinero_de_caja % 50_000
        if (dinero_de_caja>=20_000):
            queda=dinero_de_caja//20_000
            print(str(queda)+ "billete\s de 20_000 pesos")
            dinero_de_caja= dinero_de_caja % 20_000
        if (dinero_de_caja>=10_000):
            queda=dinero_de_caja//10_000
            print(str(queda)+ "billete\s de 10_000 pesos")
            dinero_de_caja= dinero_de_caja % 10_000
        if (dinero_de_caja>=5_000):
            queda=dinero_de_caja//5_000
            print(str(queda)+ "billete\s de 5_000 pesos")
            dinero_de_caja= dinero_de_caja % 5_000
        if (dinero_de_caja>=1_000):
            queda=dinero_de_caja//1_000
            print(str(queda)+ "billete\s de 1_000 pesos")
            dinero_de_caja= dinero_de_caja % 1_000
        if (dinero_de_caja>=500):
            queda=dinero_de_caja//500
            print(str(queda)+ "moneda\s de 500 pesos")
            dinero_de_caja= dinero_de_caja % 500
        if (dinero_de_caja>=200):
            queda=dinero_de_caja//200
            print(str(queda)+ "moneda\s de 200 pesos")
            dinero_de_caja= dinero_de_caja % 200
        if (dinero_de_caja>=100):
            queda=dinero_de_caja//100
            print(str(queda)+ "moneda\s de 100 pesos")
            dinero_de_caja= dinero_de_caja % 100
        if (dinero_de_caja>=10):
            queda=dinero_de_caja//10
            print(str(queda)+ "moneda\s de 10 pesos")
            dinero_de_caja= dinero_de_caja % 10
            print("Gracias por usar y confiar en cajero EAN")
elif (opcion==2):
    retiro=int(input("¿Cuánto desea retirar?: "))
    if (retiro<=dinero_de_caja):
        print("Se han retirado: ",retiro)
        dinero_de_caja=dinero_de_caja-retiro
        print("los billtes a dar son: ")
        if (retiro>=100_000):
            queda=retiro//100_000
            print(str(queda)+ "billete\s de 100_000 pesos")
            retiro=retiro % 100_000
        if (retiro>=50_000):
            queda=retiro//50_000
            print(str(queda)+ "billete\s de 50_000 pesos")
            retiro=retiro% 50_000
        if (retiro>=20_000):
            queda=retiro//20_000
            print(str(queda)+ "billete\s de 20_000 pesos")
            retiro= retiro % 20_000
        if (retiro>=10_000):
            queda=retiro//10_000
            print(str(queda)+ "billete\s de 10_000 pesos")
            retiro=retiro % 10_000
        if (retiro>=5_000):
            queda=retiro//5_000
            print(str(queda)+ "billete\s de 5_000 pesos")
            dretiro= retiro % 5_000
        if (retiro>=1_000):
            queda=retiro//1_000
            print(str(queda)+ "billete\s de 1_000 pesos")
            retiro=retiro % 1_000
        if (retiro>=500):
            queda=retiro//500
            print(str(queda)+ "moneda\s de 500 pesos")
            retiro=retiro % 500
        if (retiro>=200):
            queda=retiro//200
            print(str(queda)+ "moneda\s de 200 pesos")
            retiro=retiro % 200
        if (retiro>=100):
            queda=retiro//100
            print(str(queda)+ "moneda\s de 100 pesos")
            retiro=retiro % 100
        if (retiro>=10):
            queda=retiro//10
            print(str(queda)+ "moneda\s de 10 pesos")
            retiro=retiro % 10
        print("queda ", dinero_de_caja, "en la caja")
        print("Gracias por usar y confiar en cajero EAN")
    else:
        print("La caja no posee tal cantidad de dinero")
        print("Gracias por usar y confiar en cajero EAN")
