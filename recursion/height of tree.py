class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

        

def height(root):
    if root == None:
        return 0
    else:
        return 1+max(height(root.right),height(root.left))
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
    
print(height(root))


