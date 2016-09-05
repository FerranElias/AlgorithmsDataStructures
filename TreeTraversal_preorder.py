def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())
		
#alternatively, one can also implement preorder as a method of the BinaryTree

def preorder(self):
	print(self.key)
	if self.leftChild:
		self.leftChild.preorder()
	if self.rightChild:
		self.rightChild.preorder()
		