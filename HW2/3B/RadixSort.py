import sys
def RadixSort(A, d, k):
	result = A
	for i in range(d-1,-1,-1):
		result = CountingSort(result, k, i)
	return result


def CountingSort(A, k, d): #It receives a list of strings of the numbers with the same length

	C = []
	B = []

	for i in range(len(A)):
		B.append(str(-1))

	for i in range(k):
		C.append(0)
	for j in range(len(A)):
		C[ int(A[j][d]) ] = C[ int(A[j][d]) ] + 1
	for i in range(1,k):
		C[i] = C[i] + C[i-1]
	for j in range(len(A)-1,-1,-1):
		B[ C[ int(A[j][d]) ] - 1 ] = A[j]
		C[ int(A[j][d]) ] = C[ int(A[j][d]) ] - 1

	return B

input = sys.argv
input.pop(0)
k = int(input.pop(0))
d = int(input.pop(0))
A = RadixSort(input, d, k)
print A