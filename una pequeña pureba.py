from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter.font import BOLD, ITALIC
import random

ventanain = Tk()
ventanain.title("CAJERO EAN")
ventanain.geometry('600x500')
ventanain.config(bd=40, bg="#8A8A8A")


  usuarioc = tk.Label(ventana, text="Usuario:", bg="#60A420", fg="black")
  usuarioc.pack(pady=3, side=tk.TOP)
  entrada1 = tk.Entry(ventana)
  entrada1.pack(pady=7)
  clavec = tk.Label(ventana, text="Clave:", bg="#60A420", fg="black")
  clavec.pack(pady=3, side=tk.TOP)
  entrada2 = tk.Entry(ventana)
  entrada2.pack(pady=7)

  #
  lista=[]
  def validar():
        for a in range(0, 4):
          if (usuarios[a][0] == entrada1.get() and usuarios[a][1] == entrada2.get()):
            entidades()
            lista.append(usuarios[a][0])
            lista.append(usuarios[a][1])
            break
          else:
              messagebox.showwarning("intente de nuevo", "usuario o contraseña no validos")

                
  #dasdfiojsa0iojfd kokisdfokwajkrfaaaaaaaaaaaaaaaaaaaaaaaakdaosdpsap'0do a¿od'SVIDO'0PASO¿CDP0AS´'0CD'P´0SADCsp'0cipjsdodfjISJDFIO´0SDÓSAJDJISDFJIO´SDIFOSEDSDOIPJSAPODFPO+IKOI  PO´PIK´PIKRFGKPOFKSDOKFPIKP´SDFKP+OSKPKF+ÁOS
  dedkawpk
  dwkadp'

  def entidades():
    ventana.withdraw()
    entidades = tk.Toplevel()
    entidades.geometry("600x500")
    entidades.title("Entidades")
    entidades.config(bd=40, bg="#8A8A8A")
    loginto2 = Label(entidades, text="Seleccione su entidad", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
    loginto2.pack(pady=20)
    
    
    def banco():
      entidades.withdraw()
      banco = tk.Toplevel()
      banco.geometry("600x500")
      banco.title("Banco EAN")
      banco.configure(bd=40, bg="#1586BF")
      
      
      def saldo():
        print(lista)
        for a in range(0, 4):
            if (usuarios[a][0] == lista[0] and usuarios[a][1] == lista[1]):
                  messagebox.showinfo("Tu saldo es: ",usuarios[a][3])
                  break
      
      botoncon = tk.Button(banco, text="Consultar su saldo", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED,command=saldo)
      botoncon.pack(pady=10)
      


      def xfa100profe():
            banco.withdraw()
            bancop = tk.Toplevel()
            bancop.geometry("600x500")
            bancop.title("Retiro EAN")
            bancop.configure(bd=40, bg="#765048")
            reti= Label(bancop, text="Digite el la cantidad que quiere retirar", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED) 
            reti.pack(pady=25)
            clavecd= tk.Label(bancop, text="Monto:", bg="#60A420", fg="black")
            clavecd.pack(pady=3, side=tk.TOP)
            entrada200 = tk.Entry(bancop)
            
            entrada200.pack(pady=7)
            saldo=0
            def profe100():
                  for a in range(0, 4):
                    if (usuarios[a][0] == lista[0] and usuarios[a][1] == lista[1]):
                          usuarios[a][3]=usuarios[a][3]-int(entrada200.get())
                          saldo=usuarios[a][3]
                          break
                  messagebox.showinfo("Retiro exitoso",saldo)
            boton2222= Button(bancop, text="Retirar ", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=profe100)
            boton2222.pack(padx=20, pady=30)
            

          
      botonpar100 = Button(banco, text='retiro', font=("ARIAL", 15), fg="black", command=xfa100profe)
      botonpar100.pack(padx=20, pady=30)
      


      def opcionesimpar():
            banco.withdraw()
            bancoop = tk.Toplevel()
            bancoop.geometry("600x500")
            bancoop.title("Transferir EAN")
            bancoop.configure(bd=40, bg="#765048")
            reti= Label(bancoop, text="Digite el la cantidad que quiere transferir", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED) 
            reti.pack(pady=25)
            entrada69 = tk.Label(bancoop, text="Usuario:", bg="#60A420", fg="black")
            entrada69.pack(pady=3, side=tk.TOP)
            entrada70 = tk.Entry(bancoop)
            entrada70.pack(pady=7)
            clavecd= tk.Label(bancoop, text="Monto:", bg="#60A420", fg="black")
            clavecd.pack(pady=3, side=tk.TOP)
            entrada200 = tk.Entry(bancoop)
            entrada200.pack(pady=7)
            def retiro():
                  for a in range(0, 4):
                        if (usuarios[a][0] == lista[0] and usuarios[a][1] == lista[1]):
                          usuarios[a][3]=usuarios[a][3]-int(entrada200.get())
                          saldo=usuarios[a][3]
                          break
                  messagebox.showinfo("Transferencia exitosa",saldo)
            boton2222= Button(bancoop, text="Transferir", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=retiro)
            boton2222.pack(padx=20, pady=30)
            

          
      botonpar = Button(banco, text='Transferir', font=("ARIAL", 15), fg="black", command=opcionesimpar)
      botonpar.pack(padx=20, pady=30)
      

    def Parqueadero():
      entidades.withdraw()
      Parqueadero = tk.Toplevel()
      Parqueadero.geometry("600x500")
      Parqueadero.title("Parqueadero EAN")
      Parqueadero.configure(bd=40, bg="#FFF8DC")

      opciones = Label(Parqueadero, text="Digite el la cantidad que hay en la caja", font=("Bahnschrift SemiBold Condensed", 25, BOLD), bg="orange", fg="#00FFFF", width="40", height=2, bd=8, relief=RAISED)
      opciones.pack(pady=25)

      entrada3 = tk.Entry(Parqueadero)
      entrada3.pack()

      def opcionespar():
        Parqueadero.withdraw()
        Parqueaderoop = tk.Toplevel()
        Parqueaderoop.geometry("600x500")
        Parqueaderoop.title("Parqueadero EAN")
        Parqueaderoop.configure(bd=40, bg="#00c3d3")

        def sextosentido():
          cantidad=tk.Toplevel()
          cantidad.geometry("300x300")
          cantidad.title("cantidad")
          cantidad.configure(bd=40, bg="#765048")
          dinerocaja = Label(cantidad, text="El dinero en caja es de", font=("Bahnschrift SemiBold Condensed", 15, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocaja.pack(pady=25)
          dineroc = Label(cantidad,text=str(entrada3.get())) 
          dineroc.pack(pady=25)
          dinero_de_caja = int(entrada3.get()) 
          
          if (dinero_de_caja >= 100_000):
            queda = dinero_de_caja//100_000
            print(str(queda) + "billete\s de 100_000 pesos")
            dinero_de_caja = dinero_de_caja % 100_000
          if (dinero_de_caja >= 50_000):
            queda = dinero_de_caja//50_000
            print(str(queda) + "billete\s de 50_000 pesos")
            dinero_de_caja = dinero_de_caja % 50_000
          if (dinero_de_caja >= 20_000):
            queda = dinero_de_caja//20_000
            print(str(queda) + "billete\s de 20_000 pesos")
            dinero_de_caja = dinero_de_caja % 20_000
          if (dinero_de_caja >= 10_000):
            queda = dinero_de_caja//10_000
            print(str(queda) + "billete\s de 10_000 pesos")
            dinero_de_caja = dinero_de_caja % 10_000
          if (dinero_de_caja >= 5_000):
            queda = dinero_de_caja//5_000
            print(str(queda) + "billete\s de 5_000 pesos")
            dinero_de_caja = dinero_de_caja % 5_000
          if (dinero_de_caja >= 1_000):
            queda = dinero_de_caja//1_000
            print(str(queda) + "billete\s de 1_000 pesos")
            dinero_de_caja = dinero_de_caja % 1_000
          if (dinero_de_caja >= 500):
            queda = dinero_de_caja//500
            print(str(queda) + "moneda\s de 500 pesos")
            dinero_de_caja = dinero_de_caja % 500
          if (dinero_de_caja >= 200):
            queda = dinero_de_caja//200
            print(str(queda) + "moneda\s de 200 pesos")
            dinero_de_caja = dinero_de_caja % 200
          if (dinero_de_caja >= 100):
            queda = dinero_de_caja//100
            print(str(queda) + "moneda\s de 100 pesos")
            dinero_de_caja = dinero_de_caja % 100
          if (dinero_de_caja >= 10):
            queda = dinero_de_caja//10
            print(str(queda) + "moneda\s de 10 pesos")
            dinero_de_caja = dinero_de_caja % 10
  
        def cambiospues():
          Parqueaderoop.withdraw()
          vueltas = tk.Toplevel()
          vueltas.geometry("400x300")
          vueltas.title("Vueltas")
          vueltas.configure(bd=40, bg="#765048")
          dinerocaja = Label(vueltas, text="El dinero a dar es ", font=("Bahnschrift SemiBold Condensed", 18, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocaja.pack(pady=25)
          vueltass = Label(vueltas,text=int(entrada4.get())) 
          vueltass.pack(pady=25)
          retiro= int(entrada4.get()) 
          dinero_de_caja = int(entrada3.get()) 
          if (retiro<=dinero_de_caja):
            if (retiro >= 100_000):
              queda = retiro//100_000
              print(str(queda) + "billete\s de 100_000 pesos")
              retiro = retiro % 100_000
            if (retiro >= 50_000):
              queda = retiro//50_000
              print(str(queda) + "billete\s de 50_000 pesos")
              retiro = retiro % 50_000
            if (retiro >= 20_000):
              queda = retiro//20_000
              print(str(queda) + "billete\s de 20_000 pesos")
              retiro = retiro % 20_000
            if (retiro >= 10_000):
              queda = retiro//10_000
              print(str(queda) + "billete\s de 10_000 pesos")
              retiro = retiro % 10_000
            if (retiro >= 5_000):
              queda = retiro//5_000
              print(str(queda) + "billete\s de 5_000 pesos")
              retiro = retiro % 5_000
            if (retiro >= 1_000):
              queda = retiro//1_000
              print(str(queda) + "billete\s de 1_000 pesos")
              retiro = retiro % 1_000
            if (retiro >= 500):
              queda = retiro//500
              print(str(queda) + "moneda\s de 500 pesos")
              retiro = retiro % 500
            if (retiro >= 200):
              queda = retiro//200
              print(str(queda) + "moneda\s de 200 pesos")
              retiro = retiro % 200
            if (retiro >= 100):
              queda = retiro//100
              print(str(queda) + "moneda\s de 100 pesos")
              retiro = retiro % 100
            if (retiro >= 10):
              queda = retiro//10
              print(str(queda) + "moneda\s de 10 pesos")
              retiro = retiro % 10
            resultado=dinero_de_caja-retiro
            print("El dinero que queda en la caja es ", resultado)
         
          
        dinerocaja = Button(Parqueaderoop, text='DINERO CAJA', font=("Bahnschrift SemiBold Condensed", 30), bg="#8d9bd7", fg="black", command=sextosentido)
        dinerocaja.pack(padx=20, pady=30)
        dasda = tk.Label(Parqueaderoop, text="Digite el dinero para dar las vueltas", font=("ARIAL", 13), bg="#a1ffff", fg="black")
        dasda.pack(pady=3, side=tk.TOP)
        entrada4 = tk.Entry(Parqueaderoop)
        entrada4.pack(pady=20)
        devueltascaja = Button(Parqueaderoop, text="Siguiente ", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=cambiospues)
        devueltascaja.pack(padx=20, pady=30)

      botonpar = Button(Parqueadero, text='Siguiente', font=("ARIAL", 15), fg="black", command=opcionespar)
      botonpar.pack(padx=20, pady=30)
      retiro = int(input("¿Cuanto desea retirar?: "))
      
###

    def restaurante():
      entidades.withdraw()
      restaurante = tk.Toplevel()
      restaurante.geometry("600x500")
      restaurante.title("Restaurante EAN")
      restaurante.configure(bd=40, bg="#0CBABA")

      opciones = Label(restaurante, text="Digite la cantidad de dinero que hay en la caja", font=("Bahnschrift SemiBold Condensed", 20, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      opciones.pack(pady=25)

      entrada3 = tk.Entry(restaurante)
      entrada3.pack()

      def opcionespares():
        restaurante.withdraw()
        restauranteop = tk.Toplevel()
        restauranteop.geometry("600x500")
        restauranteop.title("Restaurante EAN")
        restauranteop.configure(bd=40, bg="#01BAEF")

        def messirve():
          cantidades=tk.Toplevel()
          cantidades.geometry("300x300")
          cantidades.title("cantidad")
          cantidades.configure(bd=40, bg="#D4A373")
          dinerocajas = Label(cantidades, text="El dinero en caja es de", font=("Bahnschrift SemiBold Condensed", 15, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocajas.pack(pady=25)
          dineroca = Label(cantidades,text=str(entrada3.get())) 
          dineroca.pack(pady=25)
          dinero_de_caja = int(entrada3.get()) 
          if (dinero_de_caja >= 100_000):
            queda = dinero_de_caja//100_000
            print(str(queda) + "billete\s de 100_000 pesos")
            dinero_de_caja = dinero_de_caja % 100_000
          if (dinero_de_caja >= 50_000):
            queda = dinero_de_caja//50_000
            print(str(queda) + "billete\s de 50_000 pesos")
            dinero_de_caja = dinero_de_caja % 50_000
          if (dinero_de_caja >= 20_000):
            queda = dinero_de_caja//20_000
            print(str(queda) + "billete\s de 20_000 pesos")
            dinero_de_caja = dinero_de_caja % 20_000
          if (dinero_de_caja >= 10_000):
            queda = dinero_de_caja//10_000
            print(str(queda) + "billete\s de 10_000 pesos")
            dinero_de_caja = dinero_de_caja % 10_000
          if (dinero_de_caja >= 5_000):
            queda = dinero_de_caja//5_000
            print(str(queda) + "billete\s de 5_000 pesos")
            dinero_de_caja = dinero_de_caja % 5_000
          if (dinero_de_caja >= 1_000):
            queda = dinero_de_caja//1_000
            print(str(queda) + "billete\s de 1_000 pesos")
            dinero_de_caja = dinero_de_caja % 1_000
          if (dinero_de_caja >= 500):
            queda = dinero_de_caja//500
            print(str(queda) + "moneda\s de 500 pesos")
            dinero_de_caja = dinero_de_caja % 500
          if (dinero_de_caja >= 200):
            queda = dinero_de_caja//200
            print(str(queda) + "moneda\s de 200 pesos")
            dinero_de_caja = dinero_de_caja % 200
          if (dinero_de_caja >= 100):
            queda = dinero_de_caja//100
            print(str(queda) + "moneda\s de 100 pesos")
            dinero_de_caja = dinero_de_caja % 100
          if (dinero_de_caja >= 10):
            queda = dinero_de_caja//10
            print(str(queda) + "moneda\s de 10 pesos")
            dinero_de_caja = dinero_de_caja % 10
          

        def cambios():
          restauranteop.withdraw()
          cambios = tk.Toplevel()
          cambios.geometry("360x300")
          cambios.title("Vueltas")
          cambios.configure(bd=40, bg="#00B4D8")
          dinerocajas = Label(cambios, text="El dinero a dar es ", font=("Bahnschrift SemiBold Condensed", 15, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocajas.pack(pady=25)
          cambioss = Label(cambios,text=str(entrada4.get())) 
          cambioss.pack(pady=25)
          retiro= int(entrada4.get()) 
          dinero_de_caja = int(entrada3.get()) 
          if (retiro<=dinero_de_caja):
            if (retiro >= 100_000):
              queda = retiro//100_000
              print(str(queda) + "billete\s de 100_000 pesos")
              retiro = retiro % 100_000
            if (retiro >= 50_000):
              queda = retiro//50_000
              print(str(queda) + "billete\s de 50_000 pesos")
              retiro = retiro % 50_000
            if (retiro >= 20_000):
              queda = retiro//20_000
              print(str(queda) + "billete\s de 20_000 pesos")
              retiro = retiro % 20_000
            if (retiro >= 10_000):
              queda = retiro//10_000
              print(str(queda) + "billete\s de 10_000 pesos")
              retiro = retiro % 10_000
            if (retiro >= 5_000):
              queda = retiro//5_000
              print(str(queda) + "billete\s de 5_000 pesos")
              retiro = retiro % 5_000
            if (retiro >= 1_000):
              queda = retiro//1_000
              print(str(queda) + "billete\s de 1_000 pesos")
              retiro = retiro % 1_000
            if (retiro >= 500):
              queda = retiro//500
              print(str(queda) + "moneda\s de 500 pesos")
              retiro = retiro % 500
            if (retiro >= 200):
              queda = retiro//200
              print(str(queda) + "moneda\s de 200 pesos")
              retiro = retiro % 200
            if (retiro >= 100):
              queda = retiro//100
              print(str(queda) + "moneda\s de 100 pesos")
              retiro = retiro % 100
            if (retiro >= 10):
              queda = retiro//10
              print(str(queda) + "moneda\s de 10 pesos")
              retiro = retiro % 10
            resultado=dinero_de_caja-retiro
            print("El dinero que queda en la caja es ", resultado)
        dinerocajas = Button(restauranteop, text='Dinero Caja', font=("ARIAL", 20), fg="black", command=messirve)
        dinerocajas.pack(padx=20, pady=30)
        nea = tk.Label(restauranteop, text="Digite el dinero para dar el cambio", font=("ARIAL", 15), bg="#F77F00", fg="black")
        nea.pack(pady=3, side=tk.TOP)
        entrada4 = tk.Entry(restauranteop)
        entrada4.pack(pady=20)
        cambiocaja = Button(restauranteop, text="Siguiente ", font=(
            "Bahnschrift SemiBold Condensed", 30, ITALIC, BOLD), command=cambios)
        cambiocaja.pack(padx=20, pady=30)

      botonpar = Button(restaurante, text='Siguiente', font=("ARIAL", 20), fg="black", command=opcionespares)
      botonpar.pack(padx=20, pady=30)
      retiro = int(input("¿Cuanto desea retirar?: "))

      #
    botonbanco = tk.Button(entidades, text="Banco EAN", cursor="hand2", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=banco)
    botonbanco.pack(pady=10)
    botonparque = tk.Button(entidades, text="Parqueadero EAN", cursor="hand2", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=Parqueadero)
    botonparque.pack(pady=10)
    botonres = tk.Button(entidades, text="Restaurante EAN", cursor="hand2", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=restaurante)
    botonres.pack(pady=10)
    #


botonsig = Button(ventanain, text='Siguiente', cursor="hand2", font=("ARIAL", 15), fg="black", command=login)
botonsig.pack(padx=20, pady=30)


ventanain.mainloop()
