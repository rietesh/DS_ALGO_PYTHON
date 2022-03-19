class Node:
    def __init__(self, v = None) -> None:
        self.value = v
        self.next = None

    def isempty(self):
        return self.value==None

    def append(self, v):
        if self.isempty():
            self.value = v

        elif self.next == None:
            newnode = Node(v)
            self.next = newnode

        else:
            self.next.append(v)

    def insert(self, val, index=0):
        if self.isempty():
            self.value = val

        elif index==0:
            newnode = Node(val)
            self.value, newnode.value = newnode.value, self.value
            self.next, newnode.next = newnode, self.next
            return

        else:
            temp = self
            newnode = Node(val)
            for i in range(1, index):
                temp = temp.next
            
            newnode.next = temp.next
            temp.next = newnode
        return

    def delete(self, val):
        if self.isempty():
            return
        
        elif self.value == val:
            self.value, self.next.value = self.next.value, self.value
            self.next = self.next.next

        else:
            temp = self
            while temp.next.value != val:
                temp = temp.next

            temp.next = temp.next.next
        return

    def __str__(self) -> str:
        ll = []
        if self.isempty():
            return str(ll)
        else:
            temp = self
            ll.append(temp.value)
            while temp.next != None:
                temp = temp.next
                ll.append(temp.value)
            return(str(ll))

'''
>>> from linked_list import *
>>> l = Node()
>>> for i in range(10): 
...   l.append(i)
... 
>>> print(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l.insert(10)
>>> print(l)
[10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l.insert(15, index=5)
>>> print(l)
[10, 0, 1, 2, 3, 15, 4, 5, 6, 7, 8, 9]
>>> l.delete(10)
>>> print(l)
[0, 1, 2, 3, 15, 4, 5, 6, 7, 8, 9]
>>> l.delete(15) 
>>> print(l)     
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
'''
            
    

