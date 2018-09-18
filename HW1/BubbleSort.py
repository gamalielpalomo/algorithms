import sys

def bubble(A):
	for i in range(len(A)-2):
		j = len(A) - 1
		while j >= i + 1:
			if A[j] < A[j-1]:
				swap(A,j,j-1)
			j = j - 1

def swap(A, x, y):
	aux = A[x]
	A[x] = A[y]
	A[y] = aux

array = sys.argv
array.pop(0)
bubble(array)
print array