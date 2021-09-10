# solo se puede consultar el dinero que hay en la caja y retirarlo para darle las vueltas al cliente. Se necesita tener un inventario de los billetes y monedas que hay en la caja.
inp=input().split()
q,w,e,r,t,j,u,p=inp
q=int(q)
w=int(w)
e=int(e)
r=int(r)
t=int(t)
j=int(j)
u=int(u)
p=int(p)
#caja negra
i=(q*50000)+(w*20000)+(e*10000)+(r*5000)+(t*2000)+(j*1000)+(u*500)+(p*100)
print("La cantidad total de dinero es "+str(i))