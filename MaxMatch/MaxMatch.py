G = {(1,6),(2,6),(1,7),(3,7),(3,9),(4,7),(5,8),(5,9)}
X = [1,2,3,4,5]
Y = [6,7,8,9]

M = set()
U = X
S = set()
T = set()
P = set()
AP = set()

def vecinos(x, P):
	vx = []
	for (a,b) in G.difference(P):
		if a == x:
			vx.append(b)
	return vx

def estaEnMatch(y):
	for (a,b) in M:
		if b == y:
			print (y," está en match")
			return True
	print (y," no está en match")
	return False


def camino(P,x):
	global AP
	if not (len(AP)>0):
		vecinosX = vecinos(x, P)
		print ("Vecinos de ",x,": ",vecinosX)
		tieneVecinoLibre = False
		for vecino in vecinosX:
			if not estaEnMatch(vecino):
				#Encontramos un camino m-aumentante
				P = P.union({(x,vecino)})
				tieneVecinoLibre = True
				AP = P
				print ("Encontrado:", AP)
				break
		if not tieneVecinoLibre:
			retroceso(P, x, vecinosX)

def retroceso(P, x, vecinosX):
	for v in vecinosX:
		for (a,b) in M:
			if b == v:
				w = a
		P = P.union({(x,v)})
		P = P.union({(w,v)})
		camino(P, w)


def MaxMatch(x):
	global AP, M
	print ("\n------------ Camino aumentante de 1 ---------------")
	camino(AP,1)
	M = (AP^M)   #diferencia simetrica para actializar el matching
	print ("Matching actual: ", list(M))
	AP = set()
	print ("\n------------ Camino aumentante de 2 ---------------")
	camino(AP,2)
	M = (AP^M)
	print ("Matching actual: ", list(M))
	AP = set()
	print ("\n------------ Camino aumentante de 3 ---------------")
	camino(AP,3)
	M = (AP^M)
	print ("Matching actual: ", list(M))
	AP = set()
	print ("\n------------ Camino aumentante de 4 ---------------")
	camino(AP,4)
	M = (AP^M)
	print ("Matching actual: ", list(M))
	AP = set()
	print ("\n------------ Camino aumentante de 5 ---------------")
	camino(AP,5)
	M = (AP^M)
	print ("Matching actual: ", list(M))
	AP = set()
	
MaxMatch(1)
print (list(M))