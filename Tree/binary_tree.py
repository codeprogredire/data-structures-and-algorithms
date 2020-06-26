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
    
    def replace(self,v,new_data):
        if self.value==None:
            return
        if self.value==v:
            self.value=new_data
            return
        res1=self.left.replace(v,new_data)
        res2=self.right.replace(v,new_data)

        return res1 or res2

    def delete(self,v):
        preorder_traversal=self.preorder()
        right_most_value=preorder_traversal[-1]
        self.replace(right_most_value,None)
        self.replace(v,right_most_value)

    # Returns height : height = number of nodes in the longest path from root to a leaf 
    def height(self):
        if self.is_empty():
            return 0
        else:
            h1=self.left.height()
            h2=self.right.height()
            h=1+max(h1,h2)
            return h

    # Delete node with value v
    def delete(self,v):
        queue=[self.root]
        last=self.root
        while len(queue):
            temp=queue.pop(0)
            last=temp
            if temp.val==v:
                dNode=temp
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        dNode,last=last,dNode
        last=None

    # Returns diameter : diameter = number of nodes in the longest path between any two nodes.
    # It may or may not include the root node. 
    def diameter(self):
        if self.is_empty():
            return 0
        if self.left.is_empty() and self.right.is_empty():
            return 1
        
        d1=self.left.diameter()
        d2=self.right.diameter()
        d3=self.left.height()+1+self.right.height()

        d=max(d1,d2,d3)

        return d