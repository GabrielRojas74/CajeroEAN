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
      

