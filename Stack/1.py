'''
Stack implementation using simple Array in Python
'''

class Stack:
    def __init__(self,limit=10):
        self.stk = []
        self.limit = limit
    
    def push(self,item):
        if len(self.stk)==self.limit:
            print('Stack overflow')
        else:
            self.stk.append(item)
            print('Stack after Push operation : {}'.format(self.stk))

    def pop(self):
        if len(self.stk)==0:
            print('Stack underflow')
            return 0
        else:
            item=self.stk.pop()
            print('Stack after Pop operation : {}'.format(self.stk))
            return item

    def is_empty(self):
        return len(self.stk)==0
    
    def peek(self):
        if len(self.stk)==0:
            print('Stack underflow')
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

stack = Stack()
stack.push(10)
stack.push(11)
stack.push(12)
print(stack.peek())
print(stack.pop())
print(stack.is_empty())
print('Stack size : {}'.format(stack.size()))
stack.push(13)
print(stack.size())

            