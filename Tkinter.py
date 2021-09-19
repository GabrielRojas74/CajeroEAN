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

etiquetabienvenidos = Label(ventanain, text="Bienvenido al Cajero EAN", font=(
    "ARIAL", 30), bg="#60A420", fg="#223499", width="60", height=6, bd=4, relief=RAISED)
etiquetabienvenidos.pack()
####
usuarios = [["gabriel", "1234", "restaurante", "10_000_000"], [
    "ivan", "1213", "banco", "1000"], ["admin", "clave", "parqueadero", "19999"]]


def login():
  ventanain.withdraw()
  ventana = tk.Tk()
  ventana.title("log in")
  ventana.geometry("700x600")
  ventana.config(bd=40, bg="#8A8A8A")
  loginto = Label(ventana, text="ingrese usuario y contraseña", font=("Bahnschrift SemiBold Condensed",
                  25, ITALIC, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
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
  def validar():
    for i in usuarios(0, 4):
        for a in range(0, 4):
                if (usuarios[a][0] == entrada1.get() and usuarios[a][1] == entrada2.get()):
                    entidades()
                    break
                else:
                    messagebox.showwarning(
                      "intente de nuevo", "usuario o contraseña no validos")
                    break
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
    loginto2 = Label(entidades, text="Seleccione su entidad", font=("Bahnschrift SemiBold Condensed",
                     25, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
    loginto2.pack(pady=20)
    #

    def banco():
      entidades.withdraw()
      banco = tk.Toplevel()
      banco.geometry("600x500")
      banco.title("Banco EAN")
      banco.configure(bd=40, bg="#1586BF")
      for i in usuarios:
          for x in range(0, 4):

              dinero = i[1]
      consultar = Label(banco, text="Consultar su saldo", font=("Bahnschrift SemiBold Condensed",
                        25, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      consultar.pack(pady=25)

      messagebox.showinfo("Saldo", "Tu saldo es de "+dinero)

      Retirar = Label(banco, text="Retiro", font=("Bahnschrift SemiBold Condensed", 25, BOLD),
                      bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      Retirar.pack(pady=25)
      messagebox.askokcancel("Retirar", "Retirando monto")

      Transferir = Label(banco, text="Transferir dinero", font=("Bahnschrift SemiBold Condensed",
                         25, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      Transferir.pack(pady=25)

      messagebox.askquestion("Transferir", "¿Esta seguro de tranferirlo?")
      messagebox.askokcancel("Tranferiendo", "Enviendo el dinero")

    def Parqueadero():
      entidades.withdraw()
      Parqueadero = tk.Toplevel()
      Parqueadero.geometry("600x500")
      Parqueadero.title("Parqueadero EAN")
      Parqueadero.configure(bd=40, bg="#765048")

    def restaurante():
      entidades.withdraw()
      restaurante = tk.Toplevel()
      restaurante.geometry("600x500")
      restaurante.title("Restaurante EAN")
      restaurante.configure(bd=40, bg="#CD3618")

      #
    botonbanco = tk.Button(entidades, text="Banco EAN", font=(
        "Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=banco)
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
