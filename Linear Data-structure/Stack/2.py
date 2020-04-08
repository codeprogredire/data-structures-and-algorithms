'''
Stack implementation using Dynamic Array. 
(Doubling array size to combat Stack overflow)
'''

class Stack:
    def __init__(self,limit=3):
        self.stk = limit*[]
        self.limit = limit

    def is_empty(self):
        return len(self.stk)

    def push(self,item):
        if len(self.stk)==0:
            self.resize()
        self.stk.append(item)
        print('Stack after Push operation : {}'.format(self.stk))

    def resize(self):
        newstk = list(self.stk)
        self.limit = 2*self.limit
        self.stk = newstk
    
    def pop(self):
        if len(self.stk)==0:
            print('Stack underflow')
            return 0
        else:
            item = self.stk.pop()
            print('Stack after Pop operation : {}'.format(self.stk))
            return item

    def size(self):
        return len(self.stk)

    def peek(self):
        if len(self.stk)==0:
            print('Stack underflow')
            return 0
        else:
            return self.stk[-1]

stack = Stack()
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
stack.push(5)
print(stack.peek())