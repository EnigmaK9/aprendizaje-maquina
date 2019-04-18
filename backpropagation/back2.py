import numpy as np
import pylab as pl
import random as rd

def creaLista():
	lista=[]
	i=-2
	while i<=2:
		lista.append(i)
		i+=0.2
	return lista

#Condiciones iniciales.
a=creaLista()

alpha=float(raw_input("Ingrese el learning rate:"))
neuronas=int(raw_input("Ingrese el numero de neuronas:"))
if neuronas==2:
	w1=[-0.27,-0.41]
	b1=[-0.48,-0.13]
	w2=[0.09,-0.17]
	b2=0.48
else:
	w1=[rd.uniform(-0.5,0.5) for _ in range(neuronas)]
	w2=[rd.uniform(-0.5,0.5) for _ in range(neuronas)]
	b1=[rd.uniform(-0.5,0.5) for _ in range(neuronas)]
	b2=rd.uniform(-0.5,0.5)


def logsig(x):
	return 1/(1+np.exp(-x))

def objetivo(p):
	return 1+np.sin((np.pi/4)*p)

def Dlgsg(x):
	return (1-logsig(x))*logsig(x)

def forward1(w1,p,b1):
	lista=[]
	for i in range(len(w1)):
		lista.append(logsig(w1[i]*p+b1[i]))
	return lista

def forward2(w2,f1,b2):
	n=0
	for i in range(len(w2)):
		n=n+(w2[i]*f1[i])
	n=n+b2
	return n

def error(p,f2):
	return objetivo(p)-f2

def s_2(p,f2):
	return -2*(error(p,f2))

def s_1(w2,f1,s2):
	lista=[]
	for i in range(len(w2)):
		lista.append(Dlgsg(f1[i])*w2[i]*s2)
	return lista

def uw_2(w2,alpha,s2,f1):
	lista=[]
	for i in range(len(w2)):
		lista.append(w2[i]-alpha*s2*f1[i])
	return lista

def uw_1(w1,alpha,s1,f):
	lista=[]
	for i in range(len(w1)):
		lista.append(w1[i]-alpha*s1[i]*f)
	return lista

def ub_2(b,alpha,s):
	return b-alpha*s

def ub_1(b,alpha,s):
	lista=[]
	for i in range(len(b)):
		lista.append(b[i]-s[i]*alpha)
	return lista

def obtienePuntos(lista,valor):
	return lista.append(valor)



it=0
it0=[]
it1=[]
itn=[]
e=1
while(e>0.001):
	itn=[]
	for valor in a:
		#print "valor={}".format(valor)
		f1=forward1(w1,valor,b1)
		f2=forward2(w2,f1,b2)
		e=error(valor,f2)
	#	print "error={} it={}".format(e,it)
		s2=s_2(valor,f2)
		s1=s_1(w2,f1,s2)
		w1=uw_1(w1,alpha,s1,valor)
		w2=uw_2(w2,alpha,s2,f1)
		b2=ub_2(b2,alpha,s2)
		b1=ub_1(b1,alpha,s1)
		if it==0:
			it0.append(f2)
		if it==1:
			it1.append(f2)
		if alpha!=1:
			itn.append(f2)
	print "iteracion={}".format(it)
	it+=1
#	if it==300000:
#		break

# print "it={}".format(it)
# print "f1={}".format(f1)
# print "f2={}".format(f2)
# print "s1={}".format(s1)
# print "s2={}".format(s2)
# print "w1={}".format(w1)
# print "w2={}".format(w2)
# print "b1={}".format(b1)
# print "b2={}".format(b2)
# print "error={}".format(e)
#print it0

#Crear gr'aficas
t = np.linspace(-2, 2, 21,endpoint=True)
pl.plot(t,objetivo(t),label="f(p)")
pl.plot(t,it0,label="it0")
if alpha!=1:
	pl.plot(t,it1,label="it1")
	pl.plot(t,itn,label="it{}".format(it))
pl.legend()
pl.show()




