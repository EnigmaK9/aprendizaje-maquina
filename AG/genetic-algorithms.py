import random


def compLis(l):

    while len(l) != 4:
        l.append(0)

def convBin(coef):


    valores = []
    while coef // 2 != 0:
        valores.append(coef % 2)
        coef = coef // 2
    if coef > 0:
        valores.append(coef)
    compLis(valores)
    valores.reverse()
    return valores

# Función para seleccionar números correctos
a = 0
b = 0
c = 0
d = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
gan = 0
sumaAptitudes = 0
f_tot = 0
pobBin = []
pobDec = []
listaEvaluacion = []
listaEsperado = []
listaAcumulado = []


def valNums(a, b, c, d):


    return False if ((a + b + c + d) <= 10 and (a + b + c + d) != 0) else True


def asignaVal():


    global a, b, c, d

    while valNums(a, b, c, d):
        a = random.randint(0, 11)
        b = random.randint(0, 11 - a)
        c = random.randint(0, 11 - a - b)
        d = random.randint(0, 11 - a - b - c)
        return a + b + c + d


def ganancia():


    global t1, t2, t3, t4, a, b, c, d, gan
    ga = [0, 0.28, 0.45, 0.65, 0.78, 0.90, 1.02, 1.13, 1.23, 1.32, 1.38]
    gb = [0, 0.25, 0.41, 0.55, 0.65, 0.75, 0.80, 0.85, 0.88, 0.90, 0.90]
    gc = [0, 0.15, 0.25, 0.40, 0.50, 0.62, 0.73, 0.82, 0.90, 0.96, 1.00]
    gd = [0, 0.20, 0.33, 0.42, 0.48, 0.53, 0.56, 0.58, 0.60, 0.60, 0.60]
    t1 = ga[a]
    t2 = gb[b]
    t3 = gc[c]
    t4 = gd[d]
    return t1 + t2 + t3 + t4


def f_objetivo():


    global gan, a, b, c, d
    gan = ganancia()
    v = abs(a + b + c + d - 10)
    return gan / ((500 * v) + 1)

# Crea individuos


def creaIndividuoBin():


    global a, b, c, d
    l = []
    a = 0
    b = 0
    c = 0
    d = 0
    asignaVal()
    l.append(convBin(a))
    l.append(convBin(b))
    l.append(convBin(c))
    l.append(convBin(d))
    return l


def creaIndividuoDec():


    global a, b, c, d
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    return l

# Inicializa población, 50 individuos.


def creaPoblacion():


    global pobBin, pobDec
    for i in range(50):
        pobBin.append(creaIndividuoBin())
        pobDec.append(creaIndividuoDec())
    evaluaIn()

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


def reemplazaPadres(p1, p2):

    global pobBin, pobDec
    h1 = []
    h2 = []
    for i in range(4):
        h1.append(p1[i][:2] + p2[i][2:])
        h2.append(p2[i][:2] + p1[i][2:])
        pobBin.append(h1)
        pobBin.append(h2)
        pobDec.append([int("".join(str(x) for x in h1[0]), 2), int("".join(str(x) for x in h1[1]), 2), int(
            "".join(str(x) for x in h1[2]), 2), int("".join(str(x) for x in h1[3]), 2)])
        pobDec.append([int("".join(str(x) for x in h2[0]), 2), int("".join(str(x) for x in h2[1]), 2), int(
            "".join(str(x) for x in h2[2]), 2), int("".join(str(x) for x in h2[3]), 2)])

# Operador mutacion
# Elige aleatoriamente un gen de un individuo y lo cambia por otro valor.


def mutacion():


    global pobBin, pobDec
    for i in range(len(pobBin)):
        for j in range(len(pobBin[i])):
            if random.random() <= 0.01:
                gen = random.randint(0, 3)
            if pobBin[i][j][gen] == 0:
                pobBin[i][j][gen] = 1
            else:
                pobBin[i][j][gen] = 0
                pobDec[i] = [
            int(
            "".join(
            str(x) for x in pobBin[i][0]), 2), int(
            "".join(
                str(x) for x in pobBin[i][1]), 2), int(
                            "".join(
                                str(x) for x in pobBin[i][2]), 2), int(
                                    "".join(
                                        str(x) for x in pobBin[i][3]), 2)]

# Inicia programa
creaPoblacion()
for i in range(100):
    sumaAptitudes = 0
    listaEvaluacion = []
    listaEsperado = []
    listaAcumulado = []
for j in range(50):
    evaluaIn()
    sumaApt()
    valorEsperado()
    valorAcumulado()
    seleccion()
for j in range(0, 50, 2):
    reemplazaPadres(pobBin[j], pobBin[j + 1])
    mutacion()
    print('Valores finales:')
    print('Mejor solución en binario: {}'.format(
        pobBin[listaEvaluacion.index(max(listaEvaluacion))]))
    print('Mejor solución en decimal: {}'.format(
        pobDec[listaEvaluacion.index(max(listaEvaluacion))]))
    print('Ganancia: {}'.format(max(listaEvaluacion)))
