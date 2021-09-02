from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
import random
from datetime import datetime, date, time
import webbrowser


def __init__(self, ventanain):
    ventanain = tk.Tk()
    ventanain.title("CAJERO EAN")
    ventanain.geometry('600x500')
    ventanain.config(bd=40, bg="#8A8A8A")
    #
    etiquetabienvenidos = tk.Label(ventanain, text="Bienvenido al Cajero EAN", font=("ARIAL", 30, ITALIC, BOLD), bg="#60A420", fg="#223499", width="60", height=6, bd=4, relief=RAISED)
    etiquetabienvenidos.pack()
        #
    botonsig = Button(ventanain, text='Siguiente', font=("TIMES NEW ROMAN", 12), fg="#D72828", command=self.login)
    botonsig.pack(fill=tk.X, padx=20, pady=30)

def login(self):
    ventana.withdraw()
    self.login = tk.Toplevel()
    self.login.geometry('600x500')
    self.login.config(bd=40, bg="#8A8A8A")
    etiquetalogin = tk.Label(self.login, text="ingrese usuario", font=("TIMES NEW ROMAN", 12), fg="#D72828")












