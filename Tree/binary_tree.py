class Tree:
    def __init__(self,initval=None):
        self.value=initval
        if self.value:
            self.left=Tree()
            self.right=Tree()
        else:
            self.left=None
            self.right=None
    
    # Checks whether the tree is empty or not
    def is_empty(self):
        return (self.value==None)

    # Returns inorder traversal of the tree(DFS)
    def inorder(self):
        if self.is_empty():
            return []
        else:
            return (self.left.inorder()+[self.value]+self.right.inorder())

    # Returns preorder traversal of the tree(DFS)
    def preorder(self):
        if self.is_empty():
            return []
        else:
            return ([self.value]+self.left.preorder()+self.right.preorder())
    # Returns postorder traversal of the tree (DFS)
    def postorder(self):
        if self.is_empty():
            return []
        else:
            return (self.left.postorder()+self.right.postorder()+[self.value])

    # Returns level-order traversal of the tree (BFS)
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
    
    # Asks for choice to choose different traversal options, and obliges the same
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

    
    # Inserting value, v
    def insert(self,v):
        if self.is_empty():
            self.value=v
            self.left=Tree()
            self.right=Tree()
        else:
            queue=[]
            queue.append(self)
            while(len(queue)>0):
                temp=queue[0]
                queue.pop(0)
                if temp.left.is_empty():
                    temp.left = Tree(v)
                    break
                else:
                    queue.append(temp.left)

                if temp.right.is_empty():
                    temp.right = Tree(v)
                    break
                else:
                    queue.append(temp.right)

    # Returns True if v is present, else returns False                
    def find(self,v):
        if self.value==None:
            return False
        if self.value==v:
            return True
        
        res1=self.left.find(v)
        res2=self.right.find(v)

        return res1 or res2