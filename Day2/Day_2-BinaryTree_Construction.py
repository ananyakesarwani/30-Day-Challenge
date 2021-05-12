class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

def inorderTraversal(root):

	if root is None:
		return

	inorderTraversal(root.left)
	print(root.data, end=' ')
	inorderTraversal(root.right)

def preorderTraversal(root):

	if root is None:
		return

	print(root.data, end=' ')
	preorderTraversal(root.left)
	preorderTraversal(root.right)

def construct(start, end, preorder, pIndex, dict):

	if start > end:
		return None, pIndex

	root = Node(preorder[pIndex])
	pIndex = pIndex + 1
	index = dict[root.data]
	root.left, pIndex = construct(start, index - 1, preorder, pIndex, dict)
	root.right, pIndex = construct(index + 1, end, preorder, pIndex, dict)
	return root, pIndex

def constructTree(inorder, preorder):

	dict = {}
	for i, e in enumerate(inorder):
		dict[e] = i

	pIndex = 0

	return construct(0, len(inorder) - 1, preorder, pIndex, dict)[0]


if __name__ == '__main__':
	inorder = [4, 2, 1, 7, 5, 8, 3, 6]
	preorder = [1, 2, 4, 3, 5, 7, 8, 6]

	root = constructTree(inorder, preorder)

	print("Inorder traversal ", end='')
	inorderTraversal(root)

	print("\nPreorder traversal ", end='')
	preorderTraversal(root)
