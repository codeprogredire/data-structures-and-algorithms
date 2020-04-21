class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

    def preorder(self):
        if self:
            print(self.val,end=' ')
            Node.preorder(self.left)
            Node.preorder(self.right)

    def height(self):
        if not self:
            return 0
        else:
            ht=1+max(Node.height(self.left),Node.height(self.right))
            return ht
    
    def diameter(self):
        if not self:
            return 0
        else:
            diam=max(1+Node.height(self.left)+Node.height(self.right),Node.diameter(self.left),Node.diameter(self.right))
            return diam-1


root=Node(1)
root.left=Node(2)
root.right=Node(3)
left=root.left
right=root.right

left.left=Node(4)
left.right=Node(5)

print('Pre-order traversal : ',end='')
root.preorder()
print('\nHeight : {}'.format(root.height()))
print('Diameter : {}'.format(root.diameter()))
