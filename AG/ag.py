import random

# Funcion que aniade ceros a la lista hasta que tenga una longitud de 4
def compLis(l):
	while len(l)!=4:
		l.append(0)
# Funcion que convierte un numero entero en binario y lo devuelve en forma de lista
def convBin(coef):
	valores = []
	while coef/2 != 0:
		valores.append(coef%2)
		coef=coef/2
	if coef > 0:
		valores.append(coef)
	compLis(valores)
	valores.reverse()
	return valores
#Funcion para seleccionar numeros correctos
a=0
b=0
c=0
d=0
t1=0
t2=0
t3=0
t4=0
gan=0
sumaAptitudes=0
f_tot=0
pobBin=[]
pobDec=[]
listaEvaluacion=[]
listaEsperado=[]
listaAcumulado=[]
# Funcion que devuelve True si la suma de a, b, c, d es mayor que 10 o igual a 0
def valNums(a,b,c,d):
	return False if ((a+b+c+d)<=10 and (a+b+c+d)!=0) else True

def asignaVal():
	global a,b,c,d
	while valNums(a,b,c,d):
		a=random.randint(0,11)
		b=random.randint(0,11-a)
		c=random.randint(0,11-a-b)
		d=random.randint(0,11-a-b-c)
	return a+b+c+d

def ganancia():
	global t1,t2,t3,t4,a,b,c,d,gan
	ga=[0,0.28,0.45,0.65,0.78,0.90,1.02,1.13,1.23,1.32,1.38]
	gb=[0,0.25,0.41,0.55,0.65,0.75,0.80,0.85,0.88,0.90,0.90]
	gc=[0,0.15,0.25,0.40,0.50,0.62,0.73,0.82,0.90,0.96,1.00]
	gd=[0,0.20,0.33,0.42,0.48,0.53,0.56,0.58,0.60,0.60,0.60]
	t1=ga[a]
	t2=gb[b]
	t3=gc[c]
	t4=gd[d]
	return t1+t2+t3+t4

def f_objetivo():
	global gan,a,b,c,d
	gan=ganancia()
	v=abs(a+b+c+d-10)
	return gan/((500*v)+1)

#Crea individuos
def creaIndividuoBin():
	global a,b,c,d
	l=[]
	a=0
	b=0
	c=0
	d=0
	asignaVal()
	l.append(convBin(a))
	l.append(convBin(b))
	l.append(convBin(c))
	l.append(convBin(d))
	return l

def creaIndividuoDec():
	global a,b,c,d
	l=[]
	l.append(a)
	l.append(b)
	l.append(c)
	l.append(d)
	return l

#Inicializa poblaci'on, 50 individuos.
def creaPoblacion():
	global pobBin,pobDec
	for i in range(50):
		pobBin.append(creaIndividuoBin())
		#print "a={},b={},c={},d={}".format(a,b,c,d)
		pobDec.append(creaIndividuoDec())
		#print "a={},b={},c={},d={}".format(a,b,c,d)
		evaluaIn()
	#print "Taman'o poblacion={}".format(len(pobDec))

#Evaluar a los individuos
def evaluaIn():
	global pobDec,listaEvaluacion
	listaEvaluacion.append(f_objetivo())

#Selecciona individuos Ruleta
def sumaApt():
	global listaEvaluacion,sumaAptitudes
	for i in range(len(listaEvaluacion)):
		sumaAptitudes+=listaEvaluacion[i]


def valorEsperado():
	global listaEsperado,listaEvaluacion,sumaAptitudes,f_tot
	f_tot=sumaAptitudes/50
	for i in range(len(listaEvaluacion)):
		listaEsperado.append(listaEvaluacion[i]/f_tot)
	x=0
	for i in range(len(listaEsperado)):
		x+=listaEsperado[i]
	#print "Suma lista valor esperado={}".format(x)

def valorAcumulado():
	global listaEsperado,listaAcumulado
	for i in range(len(listaEsperado)):
		listaAcumulado.append(listaEsperado[0]) if i==0 else listaAcumulado.append(listaAcumulado[i-1]+listaEsperado[i])
		#print listaAcumulado[i]
	#print "Ultimo valor listaAcumulado={}".format(listaAcumulado[49])


def seleccion():
	global listaAcumulado,pobDec
	pobNue=[]
	l=[random.uniform(0,50) for i in range(50)]
	for i in range(len(l)):
		for j in range(len(l)):
			if listaAcumulado[j]>l[i]:	
				pobNue.append(pobDec[j])
				break
	pobDec=pobNue
	#print pobDec
	#print "Taman'o poblacion en seleccion={}".format(len(pobDec))
	#print l
	
#Operador cruza: 2 puntos
#Siempre se utilizaran los mismos 2 puntos para garantizar que se
#generen 3 segmentos a intercambiar.

def cruza():
	global	listaAcumulado,pobDec
	pc=0.8
	l=[random.random() for i in range(50)]
	padres=[]
	hijos=[]
	posicionesHijos=[]
	#print "Taman'o poblacion={}".format(len(pobDec))
	for i in range(len(pobDec)):
		if pc>l[i]:	
			padres.append(pobDec[i])
			posicionesHijos.append(i)
	#print pobDec
	#print padres
	posicionesHijos.reverse()
	for i in range(len(posicionesHijos)):
		pobDec.pop(posicionesHijos[i])
	for i in range(len(padres)):
		pad1=padres[i]
		for j in range(len(padres)-1):
			pad2=padres[j]
			#print "pad1={}	pad2={}".format(pad1,pad2)
			if not valNums(pad1[0],pad2[1],pad2[2],pad1[3]):
				hijo=[pad1[0],pad2[1],pad2[2],pad1[3]]
				hijos.append(hijo)
				#print "hijo {}".format(hijo)
			else:
				hijo=[pad2[0],pad1[1],pad1[2],pad2[3]]
				hijos.append(hijo)
				#print "hijo {}".format(hijo)
	posicionesHijos.reverse()
	#print pobDec
	for i in range(len(posicionesHijos)):
		if len(pobDec)>posicionesHijos[i]:
			pobDec.insert(posicionesHijos[i],hijos[random.randint(0,len(hijos)-1)])
	#print "Separacion"
	#print pobDec
#realiza todas las combinaciones posibles de hijos y despues selecciona al azar
#cuales seran seleccionados.
	while len(pobDec)!=50:
		pobDec.append(hijos[random.randint(0,len(hijos)-1)])

	#print hijos
	#print "Taman'o Hijos={}".format(len(hijos))
	#print "Taman'o posicionesHijos={}".format(posicionesHijos)
	#print "Taman'o padres={}".format(len(padres))
	#print "Taman'o pobDec en cruza antes de elementos nuevos={}".format(len(pobDec))

#Se utilizara' mutacio'n uniforme
def mutacion():
	global pobDec
	total_genes=len(pobDec)*4
	mr=int(0.1*total_genes)
	posicionesMutacion=[]
	for i in range(mr):
		posicionesMutacion.append(random.randrange(0,total_genes))
	#print "Total de genes={}".format(total_genes)
	#print "posicionesMutacion={}".format(posicionesMutacion)
	for i in range(len(posicionesMutacion)):
		individuo=posicionesMutacion[i]/4
		#print "posicionesMutacion=={}".format(posicionesMutacion[i]/4)
		posicionInd=posicionesMutacion[i]%4
		listaElemRango=[0,1,2,3]
		#print "Posicion de individuo={}".format(posicionInd)
		listaElemRango.remove(posicionInd)
		#print "listaElemRango={}".format(listaElemRango)
		UB=10
		#print "Elemento={}	PosicionAMutar={}".format(individuo,posicionInd)
		for i in range(len(listaElemRango)):
			UB=UB-pobDec[individuo][listaElemRango[i]]
		#print pobDec[individuo]
		#print "UB={}".format(UB)
		if UB>0:
			pobDec[individuo][posicionInd]=random.randrange(0,UB)
			#print pobDec[individuo]

def mejorIndividuo():
	mejInd=0
	posMejInd=0
	for i in range(len(listaEvaluacion)):
		if listaEvaluacion[i]>mejInd:
			mejInd=listaEvaluacion[i]
			posMejInd=i
	print "Mejor individuo={}".format(pobDec[posMejInd])

def main():
	#asignaVal()
	#print "a={},b={},c={},d={}".format(a,b,c,d)
	#print "Millones invertidos:{}".format(a+b+c+d)
	#print f_objetivo()
	#print "Crea individuo:{}".format(creaIndividuoDec())
	creaPoblacion()
	#print 
	#Se realiza 20 veces la ejecuci'on
	for i in range(20):
		evaluaIn()
		sumaApt()
		#print "Suma aptitudes={}".format(sumaAptitudes)
		valorEsperado()
		#print listaEsperado
		valorAcumulado()
		#print listaAcumulado
		seleccion()
		cruza()
		mutacion()
		#mejorIndividuo()
	mejorIndividuo()
	#print pobDec
	#print "listaEvaluacionFinal={}".format(listaEvaluacion)	#for i in range(len(pobDec)):


main()


