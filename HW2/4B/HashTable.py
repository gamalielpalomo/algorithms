import sys
import math

table = []

def DivHash(value,m):
	if m != 0:
		return int(math.floor(value%m))

def MultHash(value,m):
	a = 0.99
	return int(math.floor( m*( (value*a)%1 ) ))

def Insert(value):
	#key = DivHash(value,len(table));
	key = MultHash(value,len(table));
	table[key].append(value)

def Search(value):
	key = DivHash(value,len(table))
	for i in range(len(table[key])):
		if(table[key][i] == value):
			return key
	return -1

def PrintTable():
	for i in range(len(table)):
		print(table[i])

input = sys.argv
input.pop(0)
m = int(input.pop(0))
for i in range(m):
	table.append([])
if m > 0:
	for i in range(len(input)):
		Insert(int(input[i]))
PrintTable()