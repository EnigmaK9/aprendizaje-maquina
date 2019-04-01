try:
	import Tkinter
except ImportError:
	raise ImportError,"Se debe instalar el modulo Tkinter"

vector = [0 for i in range(42)]
#print vector

def insertaValor(posicion, boton):
	if vector[posicion]==0:		
		vector[posicion]=1
		boton.configure(text="1")
		boton.configure(highlightbackground="black")
		print "Vector actual"
		print vector
	else:
		vector[posicion]=0
		boton.configure(text="0")
		boton.configure(highlightbackground="white")
		print "Vector actual"
		print vector

def reconoce():
	print "Algoritmo para reconocer"

root=Tkinter.Tk()
root.title("Baby apesta")
root.geometry("300x300+500-300")
etiqueta=Tkinter.Label(root, text="Introduce el patr'on dando click en los botones")
etiqueta.pack()
#Primer renglon
boton00=Tkinter.Button(root,text="0",command=lambda:insertaValor(0,boton00))
boton00.place(x=15,y=35)
boton01=Tkinter.Button(root,text="0",command=lambda:insertaValor(1,boton01))
boton01.place(x=55,y=35)
boton02=Tkinter.Button(root,text="0",command=lambda:insertaValor(2,boton02))
boton02.place(x=95,y=35)
boton03=Tkinter.Button(root,text="0",command=lambda:insertaValor(3,boton03))
boton03.place(x=135,y=35)
boton04=Tkinter.Button(root,text="0",command=lambda:insertaValor(4,boton04))
boton04.place(x=175,y=35)
boton05=Tkinter.Button(root,text="0",command=lambda:insertaValor(5,boton05))
boton05.place(x=215,y=35)
#Segundo renglon
#Primer renglon
boton10=Tkinter.Button(root,text="0",command=lambda:insertaValor(6,boton10))
boton10.place(x=15,y=65)
boton11=Tkinter.Button(root,text="0",command=lambda:insertaValor(7,boton11))
boton11.place(x=55,y=65)
boton12=Tkinter.Button(root,text="0",command=lambda:insertaValor(8,boton12))
boton12.place(x=95,y=65)
boton13=Tkinter.Button(root,text="0",command=lambda:insertaValor(9,boton13))
boton13.place(x=135,y=65)
boton14=Tkinter.Button(root,text="0",command=lambda:insertaValor(10,boton14))
boton14.place(x=175,y=65)
boton15=Tkinter.Button(root,text="0",command=lambda:insertaValor(11,boton15))
boton15.place(x=215,y=65)
#Segundo renglon
#Primer renglon
boton20=Tkinter.Button(root,text="0",command=lambda:insertaValor(12,boton20))
boton20.place(x=15,y=95)
boton21=Tkinter.Button(root,text="0",command=lambda:insertaValor(13,boton21))
boton21.place(x=55,y=95)
boton22=Tkinter.Button(root,text="0",command=lambda:insertaValor(14,boton22))
boton22.place(x=95,y=95)
boton23=Tkinter.Button(root,text="0",command=lambda:insertaValor(15,boton23))
boton23.place(x=135,y=95)
boton24=Tkinter.Button(root,text="0",command=lambda:insertaValor(16,boton24))
boton24.place(x=175,y=95)
boton25=Tkinter.Button(root,text="0",command=lambda:insertaValor(17,boton25))
boton25.place(x=215,y=95)
#Segundo renglon
#Primer renglon
boton30=Tkinter.Button(root,text="0",command=lambda:insertaValor(18,boton30))
boton30.place(x=15,y=125)
boton31=Tkinter.Button(root,text="0",command=lambda:insertaValor(19,boton31))
boton31.place(x=55,y=125)
boton32=Tkinter.Button(root,text="0",command=lambda:insertaValor(20,boton32))
boton32.place(x=95,y=125)
boton33=Tkinter.Button(root,text="0",command=lambda:insertaValor(21,boton33))
boton33.place(x=135,y=125)
boton34=Tkinter.Button(root,text="0",command=lambda:insertaValor(22,boton34))
boton34.place(x=175,y=125)
boton35=Tkinter.Button(root,text="0",command=lambda:insertaValor(23,boton35))
boton35.place(x=215,y=125)
#Segundo renglon
#Primer renglon
boton40=Tkinter.Button(root,text="0",command=lambda:insertaValor(24,boton40))
boton40.place(x=15,y=155)
boton41=Tkinter.Button(root,text="0",command=lambda:insertaValor(25,boton41))
boton41.place(x=55,y=155)
boton42=Tkinter.Button(root,text="0",command=lambda:insertaValor(26,boton42))
boton42.place(x=95,y=155)
boton43=Tkinter.Button(root,text="0",command=lambda:insertaValor(27,boton43))
boton43.place(x=135,y=155)
boton44=Tkinter.Button(root,text="0",command=lambda:insertaValor(28,boton44))
boton44.place(x=175,y=155)
boton45=Tkinter.Button(root,text="0",command=lambda:insertaValor(29,boton45))
boton45.place(x=215,y=155)
#Segundo renglon
#Primer renglon
boton50=Tkinter.Button(root,text="0",command=lambda:insertaValor(30,boton50))
boton50.place(x=15,y=185)
boton51=Tkinter.Button(root,text="0",command=lambda:insertaValor(31,boton51))
boton51.place(x=55,y=185)
boton52=Tkinter.Button(root,text="0",command=lambda:insertaValor(32,boton52))
boton52.place(x=95,y=185)
boton53=Tkinter.Button(root,text="0",command=lambda:insertaValor(33,boton53))
boton53.place(x=135,y=185)
boton54=Tkinter.Button(root,text="0",command=lambda:insertaValor(34,boton54))
boton54.place(x=175,y=185)
boton55=Tkinter.Button(root,text="0",command=lambda:insertaValor(35,boton55))
boton55.place(x=215,y=185)
#Segundo renglon
#Primer renglon
boton60=Tkinter.Button(root,text="0",command=lambda:insertaValor(36,boton60))
boton60.place(x=15,y=215)
boton61=Tkinter.Button(root,text="0",command=lambda:insertaValor(37,boton61))
boton61.place(x=55,y=215)
boton62=Tkinter.Button(root,text="0",command=lambda:insertaValor(38,boton62))
boton62.place(x=95,y=215)
boton63=Tkinter.Button(root,text="0",command=lambda:insertaValor(39,boton63))
boton63.place(x=135,y=215)
boton64=Tkinter.Button(root,text="0",command=lambda:insertaValor(40,boton64))
boton64.place(x=175,y=215)
boton65=Tkinter.Button(root,text="0",command=lambda:insertaValor(41,boton65))
boton65.place(x=215,y=215)

botonPatron=Tkinter.Button(root, text="Reconoce patron", command=lambda:reconoce())
botonPatron.place(x=90,y=245)

root.mainloop()

