G = ((1,6),(2,6),(1,7),(3,7),(3,9),(4,7),(5,8),(5,9))
X = [1,2,3,4,5]
Y = [6,7,8,9]

M = set()
U = X
S = set()
T = set()
P = set()

def vecinos(x):
	vx = []
	for (a,b) in G:
		if a == x:
			vx.append(b)
	return vx

def estaEnMatch(y):
	for (a,b) in M:
		if b == y:
			return true
	return false


def camino(P,x):
	
	vecinosX = vecinos(x)
	for vecino in vecinosX:
		if estaEnMatch(vecino):
			pass
		else:
			#Encontramos un camino m-aumentante
			M = M + {(x,vecino)}

def principal():

	x = U(0)
	camino(P,x)


print( vecinos(3) )