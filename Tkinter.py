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
ventanain.config(bd=40, bg="#f0f0f0")
ean = PhotoImage(
    file="c:\\Users\\gabor\\Desktop\\GitHub\\CajeroEAN\\eanlen.gif")
lbl = Label(ventanain, image=ean)
lbl.pack(pady=20)
etiquetabienvenidos = Label(ventanain, text="Bienvenido al Cajero EAN", font=(
    "titillium", 30), bg="#3bac53", fg="black", width="60", height=3, bd=4, relief=RAISED)
etiquetabienvenidos.pack()


usuarios = [["gabriel", "1234", "restaurante", 10_000_000], ["ivan", "1213",
                                                             "banco", 90_000], ["admin", "clave", "parqueadero", 960_000], [" ", " ", " ", " "]]


def login():

  ventanain.withdraw()
  ventana = tk.Tk()
  ventana.title("log in")
  ventana.geometry("700x600")
  ventana.config(bd=40, bg="#f0f0f0")
  loginto = Label(ventana, text="Ingrese usuario y contraseña", font=(
      "titillium", 25, BOLD), bg="#3bac53", fg="black", width=40, height=2, bd=8, relief=RAISED)
  loginto.pack(pady=20)

  #
  usuarioc = tk.Label(ventana, text="Usuario", font=(
      "titillium", 17, BOLD), bg="#3bac53", fg="black")
  usuarioc.pack(pady=3, side=tk.TOP)
  entrada1 = tk.Entry(ventana, font=("titillium", 17, BOLD))
  entrada1.pack(pady=7)
  clavec = tk.Label(ventana, text="Contraseña", font=(
      "titillium", 17, BOLD), bg="#3bac53", fg="black")
  clavec.pack(pady=3, side=tk.TOP)
  entrada2 = tk.Entry(ventana, font=("titillium", 17, BOLD))
  entrada2.pack(pady=7)

  def abrirventana2():
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry("600x600")
    win.title("Crear usuario")
    win.configure(bd=40, bg="#f0f0f0")
    loginto1 = Label(win, text="Complete los datos", font=(
        "titillium", 25, BOLD), bg="#3bac53", fg="black", width=35, height=2, bd=6, relief=RAISED)
    loginto1.pack(pady=20)

    usuarionuevo = tk.Label(win, text="Usuario", font=(
        "titillium", 16), bg="#3bac53", fg="black")
    usuarionuevo.pack(pady=3, side=tk.TOP)
    entradanu = tk.Entry(win, font=("titillium", 15, BOLD))
    entradanu.pack(pady=7)
    #
    clavenu = tk.Label(win, text="Contraseña", font=(
        "titillium", 16), bg="#3bac53", fg="black")
    clavenu.pack(pady=3, side=tk.TOP)
    entradanud = tk.Entry(win, font=("titillium", 15, BOLD))
    entradanud.pack(pady=7)
    #
    enti = tk.Label(win, text="Entidad", font=(
        "titillium", 16), bg="#3bac53", fg="black")
    enti.pack(pady=3, side=tk.TOP)
    entradant = tk.Entry(win, font=("titillium", 15, BOLD))
    entradant.pack(pady=7)
    #
    cantidad = tk.Label(win, text="Cantidad de dinero (Banco)", font=(
        "titillium", 16), bg="#3bac53", fg="black")
    cantidad.pack(pady=3, side=tk.TOP)
    entradanc = tk.Entry(win, font=("titillium", 15, BOLD))
    entradanc.pack(pady=7)

    def guardar():
      liste = []
      liste.append(str(entradanu.get()))
      liste.append(str(entradanud.get()))
      liste.append(str(entradant.get()))
      liste.append(int(entradanc.get()))
      usuarios.append(liste)
      messagebox.showinfo("Registro", "Usuario registrado exitosamente")
      win.destroy()
      login()
    boton2 = tk.Button(win, text="crear",  cursor="hand2",  font=(
        "titillium", 15, BOLD), fg="black", bg="grey", command=guardar)
    boton2.pack()
    #
  lista = []

  def validar():
      for a in range(0, 5):
          if (usuarios[a][0] == entrada1.get() and usuarios[a][1] == entrada2.get()):
            entidades()
            lista.append(usuarios[a][0])
            lista.append(usuarios[a][1])
            break
          else:
              messagebox.showwarning(
                  "intente de nuevo", "usuario o contraseña no validos")

  boton3 = tk.Button(ventana, text="validar clave", cursor="hand2", font=(
      "titillium", 18), fg="black", bg="grey", command=validar)
  boton3.pack(pady=20)
  botoncrear = tk.Button(ventana, text="Crear usuario", cursor="hand2",  font=(
      "titillium", 18), fg="black", bg="grey", command=abrirventana2)
  botoncrear.pack(pady=10)

  def entidades():
    ventana.withdraw()
    entidades = tk.Toplevel()
    entidades.geometry("600x500")
    entidades.title("Entidades")
    entidades.config(bd=40, bg="#f0f0f0")
    loginto2 = Label(entidades, text="Seleccione su entidad",  font=(
        "titillium", 20, BOLD), bg="#3bac53", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
    loginto2.pack(pady=20)
    def banco():
      entidades.withdraw()
      banco = tk.Toplevel()
      banco.geometry("600x500")
      banco.title("Banco EAN")
      banco.configure(bd=40, bg="blue")
      
      
      def saldo():
          cantidad=tk.Toplevel()
          cantidad.geometry("300x300")
          cantidad.title("cantidad")
          cantidad.configure(bd=40, bg="orange")
          dinerocaja = Label(cantidad, text="Su saldo actual es de: ", font=("Bahnschrift SemiBold Condensed", 16, BOLD), bg="lightgreen", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocaja.pack(pady=25)
          print(lista)
          for a in range(0, len(usuarios)):
            if (usuarios[a][0] == lista[0] and usuarios[a][1] == lista[1]):
                  
                  break
      
          dineroc = Label(cantidad,font=("Bahnschrift SemiBold Condensed", 16),text=str(usuarios[a][3])) 
          dineroc.pack(pady=25)
          dinero_de_caja = int(usuarios[a][3]) 
      
      botoncon = tk.Button(banco, text="Consultar su saldo", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="yellow", fg="#271F26", width="40", height=2, bd=8, relief=RAISED,command=saldo)
      botoncon.pack(pady=10)
      


      def xfa100profe():
            banco.withdraw()
            bancop = tk.Toplevel()
            bancop.geometry("600x500")
            bancop.title("Retiro EAN")
            bancop.configure(bd=40, bg="#765048")
            reti= Label(bancop, text="Digite el la cantidad que quiere retirar", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED) 
            reti.pack(pady=25)
            clavecd= tk.Label(bancop, text="Monto:", font=("Bahnschrift SemiBold Condensed",17), bg="orange", fg="black")
            clavecd.pack(pady=3, side=tk.TOP)
            entrada200 = tk.Entry(bancop, font=("Bahnschrift SemiBold Condensed",15))
            
            entrada200.pack(pady=7)
            saldo=0
            def profe100():
                  bancop=tk.Toplevel()
                  bancop.geometry("300x300")
                  bancop.title("Retiro exitoso")
                  bancop.configure(bd=40, bg="pink")
                  
                  dinerocaja = Label(bancop, text="Su nuevo saldo es de: ", font=("Bahnschrift SemiBold Condensed", 15, BOLD), bg="red", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
                  dinerocaja.pack(pady=25)  
                  for a in range(0, len(usuarios)):
                    if (usuarios[a][0] == lista[0] and usuarios[a][1] == lista[1]):
                          usuarios[a][3]=usuarios[a][3]-int(entrada200.get())
                          saldo=usuarios[a][3]
                          break
                  dineroc = Label(bancop, text=str(usuarios[a][3]), font=("Bahnschrift SemiBold Condensed", 16))
                  dineroc.pack(pady=25)
                  dinero_de_caja = int(usuarios[a][3]) 

            boton2222= Button(bancop, text="Retirar ", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=profe100)
            boton2222.pack(padx=20, pady=30)
            

          
      botonpar100 = Button(banco, text='Retiro', font=("ARIAL", 15), fg="black", command=xfa100profe)
      botonpar100.pack(padx=20, pady=30)
      


      def opcionesimpar():
            banco.withdraw()
            bancoop = tk.Toplevel()
            bancoop.geometry("600x500")
            bancoop.title("Transferir EAN")
            bancoop.configure(bd=40, bg="lightblue")
            reti= Label(bancoop, text="Digite el la cantidad que quiere transferir", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="red", fg="#271F26", width="40", height=2, bd=8, relief=RAISED) 
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
                  bancop=tk.Toplevel()
                  bancop.geometry("300x300")
                  bancop.title("Transferencia exitosa")
                  bancop.configure(bd=40, bg="Magenta")
                  
                  dinerocaja = Label(bancop, text="Su nuevo saldo es de: ", font=("Bahnschrift SemiBold Condensed", 15, BOLD), bg="Violet", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
                  dinerocaja.pack(pady=25) 
                  for a in range(0, len(usuarios)):
                        if (usuarios[a][0] == lista[0] and usuarios[a][1] == lista[1]):
                          usuarios[a][3]=usuarios[a][3]-int(entrada200.get())
                          saldo=usuarios[a][3]
                          break

                  dineroc = Label(bancop,font=("Bahnschrift SemiBold Condensed", 16),text=str(usuarios[a][3])) 
                  dineroc.pack(pady=25)
                  dinero_de_caja = int(usuarios[a][3]) 
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

      opciones = Label(Parqueadero, text="Digite el la cantidad que hay en la caja", font=("Bahnschrift SemiBold Condensed", 25, BOLD), bg="orange", fg="black", width="40", height=2, bd=8, relief=RAISED)
      opciones.pack(pady=25)

      entrada3 = tk.Entry(Parqueadero, font=("Bahnschrift SemiBold Condensed", 17))
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
          dinerocaja = Label(cantidad, text="El dinero en caja es de", font=("Bahnschrift SemiBold Condensed", 18, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocaja.pack(pady=25)
          dineroc = Label(cantidad, text=str(entrada3.get()),font=("Bahnschrift SemiBold Condensed", 17))
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
          vueltass = Label(vueltas, text=int(entrada4.get()),
                           font=("Bahnschrift SemiBold Condensed", 17))
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

      entradas = tk.Entry(restaurante,font=(
          "Bahnschrift SemiBold Condensed", 16))
      entradas.pack()

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
          dinerocajas = Label(cantidades, text="El dinero en caja es de", font=("Bahnschrift SemiBold Condensed", 20, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocajas.pack(pady=25)
          dineroca = Label(cantidades, text=str(entradas.get()),font=("Bahnschrift SemiBold Condensed", 16))
          dineroca.pack(pady=25)
          dinero_de_caja = int(entradas.get()) 
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
          dinerocajas = Label(cambios, text="El dinero a dar es ", font=("Bahnschrift SemiBold Condensed", 20, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocajas.pack(pady=25)
          cambioss = Label(cambios, text=str(entradass.get()),
                           font=("Bahnschrift SemiBold Condensed", 16))
          cambioss.pack(pady=25)
          retiro= int(entradass.get()) 
          dinero_de_caja = int(entradas.get()) 
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
        dinerocajas = Button(restauranteop, text='Dinero en Caja', font=("ARIAL", 25, BOLD), bg="#FFFC50", fg="black", command=messirve)
        dinerocajas.pack(padx=20, pady=30)
        nea = tk.Label(restauranteop, text="Digite el dinero para dar el cambio", font=("ARIAL", 15), bg="#F77F00", fg="black")
        nea.pack(pady=3, side=tk.TOP)
        entradass = tk.Entry(restauranteop)
        entradass.pack(pady=20)
        cambiocaja = Button(restauranteop, text="Siguiente ", font=("Bahnschrift SemiBold Condensed", 30, ITALIC, BOLD), bg="#f4eb8f", command=cambios)
        cambiocaja.pack(padx=20, pady=30)

      botonpar = Button(restaurante, text='Siguiente', font=("Bahnschrift SemiBold Condensed", 30, ITALIC, BOLD), bg="#f4eb8f", fg="black", command=opcionespares)
      botonpar.pack(padx=20, pady=30)
      retiro = int(input("¿Cuanto desea retirar?: "))

      #
    botonbanco = tk.Button(entidades, text="Banco EAN", cursor="hand2", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), fg="black",bg="grey", command=banco)
    botonbanco.pack(pady=10)
    botonparque = tk.Button(entidades, text="Parqueadero EAN", cursor="hand2", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), fg="black",bg="grey", command=Parqueadero)
    botonparque.pack(pady=10)
    botonres = tk.Button(entidades, text="Restaurante EAN", cursor="hand2", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), fg="black",bg="grey", command=restaurante)
    botonres.pack(pady=10)
    #


botonsig = Button(ventanain, text='Siguiente', cursor="hand2", font=("ARIAL", 15), fg="black",bg="grey", command=login)
botonsig.pack(padx=20, pady=30)


ventanain.mainloop()