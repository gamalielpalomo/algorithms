import sys
from graphviz import Digraph
from VisualRBTree import TreeRender
red = "#a54f4f"
black = "#545a63"
class Node:


	def __init__(self, key, color):
		self.key 	= key
		self.color 	= color

class Tree:

	def __init__(self):
		self.nil = Node("nil", black)
		self.root = self.nil

def LEFT_ROTATE(T, x):

	y = x.right
	x.right = y.left
	
	if y.left != T.nil:
		y.left.p = x
	y.p = x.p

	if x.p == T.nil:
		T.root = y
	elif x == x.p.left:
		x.p.left = y
	else:
		x.p.right = y
	y.left = x
	x.p = y

def RIGHT_ROTATE(T,y):

	x = y.left
	y.left = x.right

	if x.right != T.nil:
		x.right.p = y
	x.p = y.p

	if y.p == T.nil:
		T.root = x
	elif y == y.p.left:
		y.p.left = x
	else:
		y.p.right = x
	x.right = y
	y.p = x

def RB_INSERT(T, z):

	y = T.nil
	x = T.root
	
	while x != T.nil:
		y = x
		if z.key < x.key:
			x = x.left
		else:
			x = x.right
	z.p = y
	
	if y == T.nil:
		T.root = z
	elif z.key < y.key:
		y.left = z
	else:
		y.right = z
	z.left = T.nil
	z.right = T.nil
	z.color = red
	RB_INSERT_FIXUP(T,z)

def RB_INSERT_FIXUP(T,z):

	while z.p.color == red:
		if z.p == z.p.p.left:
			y = z.p.p.right
			if y.color == red:
				z.p.color = black
				y.color = black
				z.p.p.color = red
				z = z.p.p
			else:
				if z == z.p.right:
					z = z.p
					LEFT_ROTATE(T,z)
				z.p.color = black
				z.p.p.color = red
				RIGHT_ROTATE(T,z.p.p)
		else:
			y = z.p.p.left
			if y.color == red:
				z.p.color = black
				y.color = black
				z.p.p.color = red
				z = z.p.p
			else:
				if z == z.p.left:
					z = z.p
					RIGHT_ROTATE(T,z)
				z.p.color = black
				z.p.p.color = red
				LEFT_ROTATE(T,z.p.p)
	T.root.color = black


def buildDigraph(T, x):
	tree.node(str(x), str(x.key), fillcolor=x.color)
	tree.node(str(x.left), str(x.left.key))
	tree.node(str(x.right), str(x.right.key))
	tree.edge(str(x),str(x.left), constraint='true')
	tree.edge(str(x),str(x.right), constraint='true')
	if x.left != T.nil:
		buildDigraph(T, x.left)
	if x.right != T.nil:
		buildDigraph(T, x.right)



RBTree = Tree()
input = sys.argv
input.pop(0)
print (input)
while len(input) > 0:
	i = input.pop(0)
	RB_INSERT(RBTree, Node(int(i), red))

tree = Digraph(node_attr={'style': 'filled', 'shape': 'ellipse'})
buildDigraph(RBTree, RBTree.root)
print(tree.source)
tree.render('output/graph.gv', view=True)