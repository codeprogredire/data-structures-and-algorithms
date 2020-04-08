class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert_at_beginning(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        self.length+=1
    
    # Insertion at nth podition means, that after insertion the node comes at n-th place
    def insert_at_middle(self,data,pos):
        if pos==0:
            self.insert_at_beginning(data)
        else:
            temp = self.head
            count = 0
            while count!=pos-1:
                temp=temp.next
                count+=1
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1
    
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            
            temp.next = Node(data)
        self.length+=1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()
    
    def delete_from_beginning(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
        self.length-=1
    
    def delete_from_end(self):
        if self.head == None:
            return
        else:
            previousnode=self.head
            currentnode=self.head

            while currentnode.next!=None:
                previousnode=currentnode
                currentnode=currentnode.next
            previousnode=None
            self.length-=1
    
    def delete_from_position(self,pos):
        count=0
        currentnode=self.head
        previousnode=self.head

        if pos > self.length or pos<0:
            return
        else:
            while currentnode.next!=None or count<pos:
                count+=1
                if count==pos:
                    previousnode.next=currentnode.next
                    self.length-=1
                    return
                else:
                    previousnode=currentnode
                    currentnode=currentnode.next
    
    # Delete Linked List
    def clear(self):
        self.head=None



llist = LinkedList()
while True:
    print('Enter 1 to insert at beginning. Enter 2 to enter in middle. Enter 3 to insert at end. Enter 4 to delete : ')
    choice = int(input())
    if choice<=3:
        data = int(input('Enter data : '))

    if choice==1:
        llist.insert_at_beginning(data)
        llist.print_list()
    elif choice==2:
        pos = int(input('Enter position : '))
        llist.insert_at_middle(data,pos)
        llist.print_list()
    elif choice==3:
        llist.insert_at_end(data)
        llist.print_list()
    else:
        ch = int(input('Enter 1 to delete from beginning. Enter 2 to delete from middle.Enter 3 to delete from end : '))
        if ch==1:
            llist.delete_from_beginning()
            llist.print_list()
        elif ch==2:
            pos = int(input('Enter position : '))
            llist.delete_from_middle(pos)
            llist.print_list()
        elif ch==3:
            llist.delete_from_end()
            llist.print_list()


