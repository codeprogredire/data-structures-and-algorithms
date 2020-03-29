'''
Python program to get minimum element from a stack
in constant time and O(n) Space complexity.
'''

class MinStack:
    def __init__(self,limit=5):
        self.stack = []
        self.supportStack = []
        self.limit = limit

    def is_emptyself():
        return not self.stack
    
    def push(self,item):
        if len(self.stack)==0:
            self.stack.append(item)
            self.supportStack.append(item)
        elif len(self.stack)==self.limit:
            self.resize()
        else:
            self.stack.append(item)
            if item<=self.supportStack[-1]:
                self.supportStack.append(item)
        print('Stack after push operation : {}'.format(self.stack))
    
    def resize(self):
        newStk=list(self.stack)
        self.limit=2*self.limit
        stack=newStk
    
    def pop(self):
        if len(self.stack)==0:
            print('Stack underflow')
            return 0
        else:
            item=self.stack.pop()
            if item==self.supportStack[-1]:
                del self.supportStack[-1]
            print('Stack after pop : {}'.format(self.stack))
            return item
    
    def getMin(self):
        if len(self.stack)==0:
            print('Stack is empty')
            return None
        else:
            return self.supportStack[-1]

    def peek(self):
        if len(self.stack)==0:
            print('Stack is empty')
            return None
        else:
            return self.stack[-1]
    
    def size(self):
        return len(self.stack)


stk=MinStack()
stk.push(3)
stk.push(2)
stk.push(4)
stk.push(1)
stk.push(9)
print(stk.getMin())
print(stk.pop())
print(stk.pop())
print(stk.getMin())