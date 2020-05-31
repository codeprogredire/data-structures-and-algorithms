'''
Link: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
'''

class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0 or self.size<index:
            return -1
        if index==0:
            if self.head is None:
                return -1
            else:
                return self.head.val
        else:
            count=0
            temp=self.head
            while count!=index and temp:
                temp=temp.next
                count+=1
            if temp:
                return temp.val
            else:
                return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index<0 or index>self.size:
            return
        newNode=Node(val)
        if index==0:
            self.addAtHead(val)
        else:
            count=1
            temp=self.head
            while count!=index and temp:
                temp=temp.next
                count+=1
            if temp:
                newNode.next=temp.next
                temp.next=newNode
                self.size+=1
            
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or self.size<index:
            return
        if index==0:
            if self.head is None:
                return
            else:
                self.head=self.head.next
        else:
            count=1
            temp=self.head
            while count!=index and temp:
                temp=temp.next
                count+=1

            if temp.next is None:
                return
            else:
                temp.next=temp.next.next
        self.size-=1
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)