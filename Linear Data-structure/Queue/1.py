'''
Simple Array implementation of Queue
'''

class Queue:
    def __init__(self,limit=5):
        self.queue = [None]*limit
        self.front = -1
        self.rear = -1
        self.limit = limit
        self.size = 0
    
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def enqueue(self,item):
        if self.front == 0 and self.rear == self.limit-1:
            print('Queue Overflow')
            return
        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear+1)%(self.limit)
        self.queue[self.rear] = item
        self.size += 1
        print('Queue after Enqueue : {}'.format(self.queue))

    

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print('Queue underflow')
            return 0
        elif self.front == self.rear: # Only one element in Queue
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = -1
            self.rear = -1
            self.size = 0
            print('Queue after Dequeue operation : {}'.format(self.queue))
            return item
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front+1)%(self.limit)
            self.size -= 1
            print('Queue after Dequeue operation : {}'.format(self.queue))
            return item
    
    def QueueSize(self):
        return self.size
        
            




queue = Queue()
while True:
    choice = int(input('Enter 1 for Enqueue. Enter 2 for Dequeue. Enter 3 for size of queue :  '))
    if choice == 1:
        n = int(input('Enter integer to Enqueue : '))
        queue.enqueue(n)
    elif choice == 2:
        print(queue.dequeue())
    else:
        print(queue.QueueSize())