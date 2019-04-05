from random import random

try:
	import Tkinter
except ImportError:
	raise ImportError,"Se debe instalar el modulo Tkinter"

D1=[1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0]
D2=[0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
D3=[0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0]
D4=[1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0]
D5=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0]

X1=[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
X2=[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1]
X3=[1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
X4=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
X5=[1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

J1=[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
J2=[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
J3=[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
J4=[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]
J5=[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]

G1=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0]
G2=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
G3=[1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
G4=[1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
G5=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0]

bias=[0.5,0.5]
w=[[random() for i in range(42)],[random() for i in range(42)]]
targets=[[0,0],[0,1],[1,0],[1,1]]
e=[1,1]
letras=[D1,D2,D3,D4,D5,X1,X2,X3,X4,X5,J1,J2,J3,J4,J5,G1,G2,G3,G4,G5]

def hardlim(n):
	a=[0,0]
	for i in range(len(n)):
		if n[i]>=0:
			a[i]=1
		else:
			a[i]=0
	return a

def error(targets,a,i):
	e=[0,0]
	if 0<=i<5:
		for j in range(len(e)):
			e[j]=targets[0][j]-a[j]
	elif 5<=i<10:
		for j in range(len(e)):
			e[j]=targets[1][j]-a[j]
	elif 10<=i<15:
		for j in range(len(e)):
			e[j]=targets[2][j]-a[j]
	elif 15<=i<20:
		for j in range(len(e)):
			e[j]=targets[3][j]-a[j]
	return e

vector = [0 for i in range(42)]
#print vector

def insertaValor(posicion, boton):
	if vector[posicion]==0:		
		vector[posicion]=1
		boton.configure(text="1")
		boton.configure(highlightbackground="black")
		boton.configure(background="black")
		#print "Vector actual"
		#print vector
	else:
		vector[posicion]=0
		boton.configure(text="0")
		boton.configure(highlightbackground="white")
		boton.configure(background="white")
		#print "Vector actual"
		#print vector

def obtieneN(w,vector,bias):
	n=[0,0]
	for i in range(len(w[0])):
		n[0]=n[0]+w[0][i]*vector[i]
		n[1]=n[1]+w[1][i]*vector[i]
	print "Imprimiendo n"
	print n
	for i in range(len(n)):
		n[i]=n[i]+bias[i]
	return n
               
def updateW(w,e,vector):
	for i in range(len(vector)):
		w[0][i]=w[0][i]+vector[i]*e[0]
		w[1][i]=w[1][i]+vector[i]*e[1]
	print "--->Imprime w {}".format(w)
	return w

def updateBias(bias,e):
	for i in range(len(bias)):
		bias[i]=bias[i]+e[i]
		print "Bias"
		print bias
	return bias

while e[0]!=0 or e[1]!=0:
	for letra in letras:
		n=obtieneN(w,letra,bias)
		a=hardlim(n)
		e=error(targets,a,letras.index(letra))
		if e[0]!=0 or e[1]!=1:
			w=updateW(w,e,letra)
			bias=updateBias(bias,e)
print "Peso despues de entrenamiento {}, bias final: {}, error= {}".format(w,bias,e)

def reconoce(vector):
	n=obtieneN(w,vector,bias)
	a=hardlim(n)
	print "-->A={}".format(a)
	print "-->n={}".format(n)
	if a==targets[0]:
		lblRes.configure(text="D")
	elif a==targets[1]:
		lblRes.configure(text="X")
	elif a==targets[2]:
		lblRes.configure(text="J")
	elif a==targets[3]:
		lblRes.configure(text="G")
		


root=Tkinter.Tk()
root.title("Reconocedor")
root.geometry("305x305+500-300")
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

botonPatron=Tkinter.Button(root, text="Reconoce patron", command=lambda:reconoce(vector))
botonPatron.place(x=90,y=245)
lblRes=Tkinter.Label(root)
lblRes.place(x=95,y=270)
root.mainloop()

