from graphviz import Digraph

class TreeRender:

	tree = Digraph();

	def __init__(self, inputTree):
		self.buildDigraph(inputTree, inputTree.root)

	def buildDigraph(self, T, x):
		self.tree.node(str(x), str(x.key))
		if x.left != T.nil:
			buildDigraph(T, x.left)
		if x.right != T.nil:
			buildDigraph(T, x.right)

	def render(self):
		self.tree.render('output/graph.gv', view=True)		


"""

tree.node('A', 'KA')
tree.node('B', 'SB')
tree.node('C', 'SL')

tree.edges(['AB','AC'])
tree.edge('B','C', constraint='false')

print(tree.source)
tree.render('output/graph.gv', view=True)"""