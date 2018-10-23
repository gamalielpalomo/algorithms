import sys
import math	

A = []
h_Size = 0

def Build_Max_Heap(d):
	for i in range (math.floor(len(A)/d)-1, -1, -1):		
		#print ("Max_Heapify(",i,")")
		Max_Heapify(d, i)

def Max_Heapify(d, i):
	first = d * i + 1
	last =  d * i + d
	largest = i
	for j in range(first, last + 1 ):
		if j < h_Size and A[j] > A[largest]:
			largest = j
	if largest != i:
		Swap(i, largest)
		Max_Heapify(d, largest)

def Swap(i, j):
	aux = A[i]
	A[i] = A[j]
	A[j] = aux

def ShowTree(d):
	for i in range (0,len(A)):
		first = d * i + 1
		last =  d * i + d
		print("\n", A[i]," -> ", end="")
		for j in range(first, last + 1 ):
			if j < h_Size:
				print(A[j]," ", end="")

input = sys.argv
input.pop(0)
d = int(input.pop(0))
h_Size = len(input)
for i in range(h_Size):
	A.append(int(input[i]))
print ("Array: ",A)
print ("Heap size: ",h_Size)
print ("Arity (d): ",d,"\n")
Build_Max_Heap(d)
print (A)
ShowTree(d)