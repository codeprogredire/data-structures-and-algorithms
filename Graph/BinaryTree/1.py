class Node:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def append(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            curr=self.root
            