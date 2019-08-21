class Tree:
    def __init__(self,initval=None):
        self.value=initval
        if self.value:
            self.left=Tree()
            self.right=Tree()
        else:
            self.left=None
            self.right=None
    
    def is_empty(self):
        return (self.value==None)

    def inorder(self):
        if self.is_empty():
            return []
        else:
            return (self.left.inorder()+[self.value]+self.right.inorder())

    def preorder(self):
        if self.is_empty():
            return []
        else:
            return ([self.value]+self.left.preorder()+self.right.preorder())

    def postorder(self):
        if self.is_empty():
            return []
        else:
            return (self.left.postorder()+self.right.postorder()+[self.value])

    def levelorder(self):
        if self.is_empty():
            return []
        
        queue=[]

        queue.append(self)

        while(len(queue)>=1):
            print(queue[0].value,end=' ')
            if not queue[0].left.is_empty():
                queue.append(queue[0].left)
            if not queue[0].right.is_empty():
                queue.append(queue[0].right)
            del(queue[0])
    
    def __str__(self):
        choice=int(input('enter 1 for inorder, 2 for preorder, 3 for postorder or 4 for level-order bst traversal: '))
        if choice==1:
            print('Inorder traversal : ', end=' ')
            return str(self.inorder())
        elif choice==2:
            print('Preorder traversal : ',end=' ')
            return str(self.preorder())
        elif choice==3:
            print('Postorder traversal : ',end=' ')
            return (str(self.postorder()))
        else:
            print('Level-order traversal : ',end='')
            return str(self.levelorder())

    def find(self,v):
        if self.value==None:
            return False
        elif self.value==v:
            return True
        elif v<self.value:
            return self.left.find(v)
        else:
            return self.right.find(v)

    # Returns minimum value of the tree
    def minval(self):
        if self.left.is_empty():
            return self.value
        else:
            return self.left.minval()

    # Returns maximum value of the tree
    def maxval(self):
        if self.right.is_empty():
            return self.value
        else:
            return self.right.maxval()

    # Inserting value, v
    def insert(self,v):
        # If value is already present, do nothing
        if self.value==v:
            return
        # If search fails,then add a new leaf
        elif self.is_empty():
            self.value=v
            self.left=Tree()
            self.right=Tree()
        # If v < self.value, then go to left subtree
        elif v<self.value:
            self.left.insert(v)
        else:
            # Goto right sub-tree
            self.right.insert(v)
    

    def delete(self,v):
        if self.is_empty():
            return
        elif v<self.value:
            self.left.delete(v)
        elif v>self.value:
            self.right.delete(v)
        else:
            # if v == self.value
            if self.is_leaf():
                self.make_empty()
            elif self.left.is_empty():
                self.copy_right()
            else:
                self.value=self.left.maxval()
                self.left.delete(self.left.maxval())

    def is_leaf(self):
        return (self.left.is_empty() and self.right.is_empty())
    
    def make_empty(self):
        self.value=None
        self.left=None
        self.right=None
    
    def copy_right(self):
        self.value=self.right.value
        self.left=self.right.left
        self.right=self.right.right