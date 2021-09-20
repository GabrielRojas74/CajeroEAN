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

etiquetabienvenidos = Label(ventanain, text="Bienvenido al Cajero EAN", font=("ARIAL", 30), bg="#60A420", fg="#223499", width="60", height=6, bd=4, relief=RAISED)
etiquetabienvenidos.pack()
####
usuarios = [["gabriel", "1234", "restaurante", 10_000_000], ["ivan", "1213", "banco", 90_000], ["admin", "clave", "parqueadero", 960_000],[" "," "," "," "]]



def login():

  ventanain.withdraw()
  ventana = tk.Tk()
  ventana.title("log in")
  ventana.geometry("700x600")
  ventana.config(bd=40, bg="#8A8A8A")
  loginto = Label(ventana, text="ingrese usuario y contraseña", font=("Bahnschrift SemiBold Condensed",25, ITALIC, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
  loginto.pack(pady=20)

  #
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

                
  boton3 = tk.Button(ventana, text="validar clave", command=validar)
  boton3.pack(pady=20)

  loginto3 = Label(ventana, text="En caso de no tener un usuario comuniquese con el administrador (018000 admin)", font=(
      "arial", 11,  BOLD), bg="#E36421", fg="black", width="90", height=2, bd=8, relief=RAISED)
  loginto3.pack(pady=80)

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
      Parqueadero.configure(bd=40, bg="#765048")

      opciones= Label(Parqueadero, text="Digite el la cantidad que hay en la caja", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED) 
      opciones.pack(pady=25)
      
      entrada3 = tk.Entry(Parqueadero)
      entrada3.pack()
      def opcionespar():
        Parqueadero.withdraw()
        Parqueaderoop = tk.Toplevel()
        Parqueaderoop.geometry("600x500")
        Parqueaderoop.title("Parqueadero EAN")
        Parqueaderoop.configure(bd=40, bg="#765048")
        def sextosentido():
          messagebox.showinfo("Caja", "El dinero de la caja es: "+ str(entrada3.get()))
        def cambiospues():
          Parqueaderoop.withdraw()
          vueltas = tk.Toplevel()
          vueltas.geometry("600x500")
          vueltas.title("Vueltas")
          vueltas.configure(bd=40, bg="#765048")

        dinerocaja = Button(Parqueaderoop, text='Dinero Caja', font=("ARIAL", 15), fg="black", command=sextosentido)
        dinerocaja.pack(padx=20, pady=30)
        dasda = tk.Label(Parqueaderoop, text="Digite el dinero para dar las vueltas", font=("ARIAL", 13) ,bg="#60A420", fg="black")
        dasda.pack(pady=3, side=tk.TOP)
        entrada4 = tk.Entry(Parqueaderoop)
        entrada4.pack(pady=20)
        devueltascaja= Button(Parqueaderoop, text="Siguiente ", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=cambiospues)
        devueltascaja.pack(padx=20, pady=30)
        
        
      botonpar = Button(Parqueadero, text='Siguiente', font=("ARIAL", 15), fg="black", command=opcionespar)
      botonpar.pack(padx=20, pady=30)
      retiro=int(input("¿Cuanto desea retirar?: "))
    
    
      

            
      

     



###

    def restaurante():
      entidades.withdraw()
      restaurante = tk.Toplevel()
      restaurante.geometry("600x500")
      restaurante.title("Restaurante EAN")
      restaurante.configure(bd=40, bg="#CD3618")


      bien = Label(restaurante, text="bienvenidos", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      bien.pack()
      Transferir = Label(restaurante, text="cuanto dinero", font=("Bahnschrift SemiBold Condensed",25, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      Transferir.pack(pady=25)
      entrada3 = tk.Entry(restaurante)
      entrada3.pack()
      
    


      #
    botonbanco = tk.Button(entidades, text="Banco EAN", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=banco)
    botonbanco.pack(pady=10)
    botonparque = tk.Button(entidades, text="Parqueadero EAN", font=(
          "Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=Parqueadero)
    botonparque.pack(pady=10)
    botonres = tk.Button(entidades, text="Restaurante EAN", font=(
          "Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=restaurante)
    botonres.pack(pady=10)
    #


botonsig = Button(ventanain, text='Siguiente', font=(
    "ARIAL", 15), fg="black", command=login)
botonsig.pack(padx=20, pady=30)


ventanain.mainloop()
