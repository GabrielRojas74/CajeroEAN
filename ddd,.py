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
"""
def validar():
    usuarios = [["gabriel", 1234, "restaurante",10_000_000], ["ivan", 1213, "banco", 1000]]
    usuario = cajanombre.get()
    contraseña = cajacontraseña.get()
    for i in usuarios:
        if (i[0] == usuario and i[1] == contraseña):

"""
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




botonsig = Button(ventanain, text='Siguiente', font=("TIMES NEW ROMAN", 12), fg="#D72828", command=login)
botonsig.pack(padx=20, pady=30)







ventanain.mainloop()
"""else:
    messagebox.showwarning("usuario o contraseña no validos", "intente de nuevo")"""
