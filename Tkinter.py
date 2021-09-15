from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter.font import BOLD, ITALIC
import random
from datetime import datetime, date, time
import webbrowser


ventanain = Tk()
ventanain.title("CAJERO EAN")
ventanain.geometry('600x500')
ventanain.config(bd=40, bg="#8A8A8A")

etiquetabienvenidos = Label(ventanain, text="Bienvenido al Cajero EAN", font=("ARIAL", 30), bg="#60A420", fg="#223499", width="60", height=6, bd=4, relief=RAISED)
etiquetabienvenidos.pack()
####

usuarios = [["gabriel", 1234, "restaurante",10_000_000], ["ivan", 1213, "banco", 1000]]
def login():
  ventanain.withdraw()
  ventana = tk.Tk()
  ventana.title("log in")
  ventana.geometry("600x500")
  ventana.config(bd=40, bg="#8A8A8A")
  loginto = Label(ventana, text="ingrese usuario y contraseña", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
  loginto.pack(pady=20)

  #
  usuarioc = tk.Label(ventana, text="Usuario:", bg="#60A420", fg="black")
  usuarioc.pack(pady=3, side=tk.TOP)
  entrada1 =tk.Entry(ventana)
  entrada1.pack(pady=7)
  clavec= tk.Label(ventana, text="Clave:", bg="#60A420", fg="black")
  clavec.pack(pady=3,side=tk.TOP)
  entrada2 = tk.Entry(ventana)
  entrada2.pack(pady=7)
  
  #
  def validar():
    for i in usuarios:
      if (entrada1 == i[0] and entrada2 == i[1]):
        abrirventana2()
      else:
        messagebox.showwarning("intente de nuevo", "usuario o contraseña no validos")
        
    
  def abrirventana2():
    ventana.withdraw()
    win = tk.Toplevel()
    win.geometry("600x500")
    win.title("Crear usuario")
    win.configure(bd=40, bg="#8A8A8A")

    def guardar_datos():
      win.withdraw()
      entidades= tk.Toplevel()
      entidades.geometry("600x500")
      entidades.title("Entidades")
      entidades.configure(bd=40, bg="#8A8A8A")
      loginto2 = Label(entidades, text="Seleccione su entidad", font=("Bahnschrift SemiBold Condensed",  25, ITALIC, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      loginto2.pack(pady=20)

      botonbanco = tk.Button(entidades, text="Banco", font=("Arial",  25))
      botonbanco.pack(pady=10)
      botonparquea = tk.Button(entidades, text="Parqueadero", font=("Arial",  25))
      botonparquea.pack(pady=10)
      botonres = tk.Button(entidades, text="Restaurante", font=("Arial",  25))
      botonres.pack(pady=10)

      messagebox.showinfo("😁", "Registrado con exito")
      
    loginto1 = Label(win, text="Complete los datos.", font=("Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
    loginto1.pack(pady=20)
    #
    usuarionuevo = tk.Label(win, text="Usuario:", bg="#60A420", fg="black")
    usuarionuevo.pack(pady=3, side=tk.TOP)
    entradanu = tk.Entry(win)
    entradanu.pack(pady=7)
    #
    clavenu = tk.Label(win, text="Clave:", bg="#60A420", fg="black")
    clavenu.pack(pady=3, side=tk.TOP)
    entradanud = tk.Entry(win)
    entradanud.pack(pady=7)
    #
    enti= tk.Label(win, text="Entidad a la que pertenece", bg="#60A420", fg="black")
    enti.pack(pady=3, side=tk.TOP)
    entradant = tk.Entry(win)
    entradant.pack(pady=7)
    #
    cantidad = tk.Label(win, text="Cantidad de dinero (banco)", bg="#60A420", fg="black")
    cantidad.pack(pady=3, side=tk.TOP)
    entradanc = tk.Entry(win)
    entradanc.pack(pady=7)

    usuario = []
    usuario.append(usuarionuevo)
    usuario.append(clavenu)
    usuario.append(cantidad)
    usuarios.append(enti)
    #
    boton2 = tk.Button(win, text="crear", command=guardar_datos)
    boton2.pack()   
        
  
  
 
  boton3 = tk.Button(ventana, text="validar clave", command=validar)
  boton3.pack()
  botoncrear = tk.Button(ventana, text="Crear usuario", command=abrirventana2)
  botoncrear.pack(pady=7)


"""
boton = tk.Button(ventana, text="nueva ventana")
  boton.pack()

 usuarios = [["gabriel", 1234, "restaurante",10_000_000], ["ivan", 1213, "banco", 1000]]
    usuario = cajanombre.get()
    contraseña = cajacontraseña.get()
    for i in usuarios:
        if (i[0] == usuario and i[1] == contraseña):
 
def login():
    ventanain.withdraw()
    login = Toplevel()
    login.geometry('600x500')
    login.config(bd=40, bg="#8A8A8A")
    loginto = Label(login, text="ingrese usuario y contraseña", font=("TIMES NEW ROMAN", 12), fg="#D72828")
    loginto.pack()

    cajatxtnombre = tkinter.Entry(login, font="arial 20")
    cajatxtnombre.pack(padx=20, pady=20)
    cajatxtcontraseña = tkinter.Entry(login, font="arial 20")
    cajatxtcontraseña.pack(padx=20, pady=20)
    def cajatxt():
        usuarios = [["gabriel", 1234, "restaurante", 10_000_000], ["ivan", 1213, "banco", 1000]]
        usuario=cajatxtnombre.get()
        contraseña=cajatxtcontraseña.get()
        for i in usuarios:
            if (i[0] == usuario and i[1] == contraseña):
                
                def ingresar():
                    login.withdraw()
                    ingresar = Toplevel()
                    ingresar.geometry('600x500')
                    ingresar.config(bd=40, bg="#8A8A8A")
                    ingresarm = Label(login, text="ingrese usuario y contraseña", font=(
                        "TIMES NEW ROMAN", 12), fg="#D72828")
                    ingresarm.pack()
                    
            else:
                messagebox.showwarning("usuario o contraseña no validos", "intente de nuevo")

        botonin = Button(login, text='ingresar', font=("TIMES NEW ROMAN", 12), fg="#D72828", command=ingresar)
        botonin.pack(padx=20, pady=30)
               
            
    def cre():
        login.withdraw()
        cre = Toplevel()
        cre.geometry('600x500')
        cre.config(bd=40, bg="#8A8A8A")
        creto = Label(login, text="ingrese usuario y contraseña",font=("TIMES NEW ROMAN", 12), fg="#D72828")
        creto.pack()



    
    botoncr = Button(login, text='crear usuario', font=("TIMES NEW ROMAN", 12), fg="#D72828", command=cre)
    botoncr.pack(padx=20, pady=30)


"""

botonsig = Button(ventanain, text='Siguiente', font=("TIMES NEW ROMAN", 12), fg="#D72828", command=login)
botonsig.pack(padx=20, pady=30)







ventanain.mainloop()
"""else:
    messagebox.showwarning("usuario o contraseña no validos", "intente de nuevo")"""
