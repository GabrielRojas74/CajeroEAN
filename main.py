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
          retiro=int(input("¿Cuanto desea retirar?: "))
          retiro=entrada4
          if (retiro<=entrada3):
            messagebox.showinfo("Vueltas", "Las vueltas son: "+ str(entrada3.get()))
          if (retiro>=100_000):
                queda=retiro//100_000
                queda=Label(cambiospues,(str(queda))+ "billete\s de 100_000 pesos")
                queda.pack()
                retiro=retiro % 100_000 
          if (retiro>=50_000):
                queda=retiro//50_000
                queda=Label(cambiospues,(str(queda))+ "billete\s de 50_000 pesos")
                queda.pack()
                retiro=retiro% 50_000
          if (retiro>=20_000):
                queda=retiro//20_000
                queda=Label(cambiospues,(str(queda))+ "billete\s de 20_000 pesos")
                queda.pack()
                retiro= retiro % 20_000
          if (retiro>=10_000):
                queda=retiro//10_000
                queda=Label(cambiospues,(str(queda))+ "billete\s de 10_000 pesos")
                queda.pack()
                retiro=retiro % 10_000
          if (retiro>=5_000):
                queda=retiro//5_000
                queda=Label(cambiospues,(str(queda))+ "billete\s de 5_000 pesos")
                queda.pack()
                dretiro= retiro % 5_000
          if (retiro>=1_000):
                queda=retiro//1_000
                queda=Label(cambiospues,(str(queda))+ "billete\s de 1_000 pesos")
                queda.pack()
                retiro=retiro % 1_000
          if (retiro>=500):
                queda=retiro//500
                queda=Label(cambiospues,(str(queda))+ "moneda\s de 500 pesos")
                queda.pack()
                retiro=retiro % 500
          if (retiro>=200):
                queda=retiro//200
                queda=Label(cambiospues,(str(queda))+ "moneda\s de 200 pesos")
                queda.pack()
                retiro=retiro % 200
          if (retiro>=100):
                queda=retiro//100
                queda=Label(cambiospues,(str(queda))+ "moneda\s de 100 pesos")
                queda.pack()
                retiro=retiro % 100
          if (retiro>=10):
                queda=retiro//10
                queda=Label(cambiospues,(str(queda))+ "moneda\s de 10 pesos")
                queda.pack()
                retiro=retiro % 10
          
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
