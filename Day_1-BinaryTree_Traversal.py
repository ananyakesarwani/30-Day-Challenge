class Node:   
   def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

   def insert(self, val):

        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
            else:
                self.val = val

   def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.val,end=', ')
            self.inorderTraversal(root.right)
   def preorderTraversal(self, root):
        if root:
            print(root.val,end=', ')
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
   def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.val,end=', ')
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print("\nInorder traversal")
print(root.inorderTraversal(root))
print("\nPreorder traversal")
print(root.preorderTraversal(root))
print("\nPostorder traversal")
print(root.postorderTraversal(root))
