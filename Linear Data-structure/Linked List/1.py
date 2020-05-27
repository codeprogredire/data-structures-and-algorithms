'''
Singly Linked List Implementation
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next

            temp.next=newNode

    def insert_at_beginning(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    
    #Insert at position n means, that data comes at n-th position after insertion.
    def insert_at_middle(self,data,pos):
        if self.head is None:
            self.insert_at_beginning(data)
        else:
            newNode=Node(data)
            count=1
            temp=self.head
            while count!=pos:
                temp=temp.next
                count+=1
            newNode.next=temp.next
            temp.next=newNode
    
    def printlist(self):
        if self.head==None:
            print('Empty Linked List')
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=' ')
                temp=temp.next
            print()

    def delete_from_front(self):
        if self.head is None:
            pass
        else:
            self.head=self.head.next

    def delete_from_end(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp.next=None
    
    def delete_from_middle(self,pos):
        if pos==0:
            self.delete_from_front()
        else:
            count=1
            temp=self.head
            while count!=pos and temp:
                temp=temp.next
                count+=1
            if temp.next is None:
                print('Invalid pos parameter')
            else:
                temp.next=temp.next.next





llist=LinkedList()
llist.append(1)
llist.append(5)
llist.append(15)
llist.append(51)
llist.printlist()
llist.insert_at_beginning(0)
llist.printlist()
llist.insert_at_middle(3,3)
llist.printlist()
llist.delete_from_front()
llist.printlist()
llist.delete_from_end()
llist.printlist()
llist.delete_from_middle(2)
llist.printlist()
llist.delete_from_middle(2)
llist.printlist()
llist.delete_from_middle(2)
llist.printlist()
llist.delete_from_middle(1)
llist.printlist()
