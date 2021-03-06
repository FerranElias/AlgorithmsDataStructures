def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())
		
#the next function evaluates a tree

def postordereval(tree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	res1 = None
	res2 = None
	if tree:
		res1 = postordereval(tree.getLeftChild())
		res2 = postordereval(tree.getRightChild())
		if res1 and res2:
			return opers[tree.getRootVal()](res1,res2)
		else:
			return tree.getRootVal()
