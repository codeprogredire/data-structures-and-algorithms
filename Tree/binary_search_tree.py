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

    # Finds the element v recursively
    def rec_find(self,v):
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
    
    # deletes the value v from the tree
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

    # Checks whether the node in question is a leaf node or not
    def is_leaf(self):
        return (self.left.is_empty() and self.right.is_empty())
    
    # Make the node empty
    def make_empty(self):
        self.value=None
        self.left=None
        self.right=None
    
    # Copy the contents of the right child of the current node into the current node
    def copy_right(self):
        self.value=self.right.value
        self.left=self.right.left
        self.right=self.right.right


    # Iterative implementation of find function
    def iter_find(self,v):
        while(self.value!=v and not self.is_empty()):
            if v<self.value:
                self=self.left
            else:
                self=self.right
        
        if v==self.value:
            return True
        else:
            return False

    # Returns lowest common ancestors between n1 and n2
    def lca(self,n1,n2):
        walk_2_n1=self.path(n1)
        walk_2_n2=self.path(n2)
        common_nodes=set(walk_2_n1).intersection(set(walk_2_n2))
        lowest_common_ancestor=[n1 for n1 in walk_2_n1 for n2 in walk_2_n2 if n1==n2][-1]
        return lowest_common_ancestor

    # Returns the path from root to node v
    def path(self,v):
        walk=[]
        while(self.value!=v):
            walk.append(self.value)
            if v<self.value:
                self=self.left
            else:
                self=self.right
        walk.append(self.value)

        return walk

    # Second approach to find Lowest common ancestor
    def lca2(self,n1,n2):
        if not (self.iter_find(n1) and self.iter_find(n2)):
            print('{} or {} is not present. Please enter correct values.'.format(n1,n2))
            return
        n1=min(n1,n2)
        n2=max(n1,n2)
        while(not self.is_empty()):
            if (self.value>n1 and self.value>n2):
                self=self.left
            elif (self.value<n1 and self.value<n2):
                self=self.right
            else:
                break

        return self.value