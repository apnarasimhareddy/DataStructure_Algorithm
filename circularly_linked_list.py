class Circularly_Linked_List:
    class _Node:
        def __init__(self,element,next):
            self._element=element
            self._next=next

    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise Exception("Circularly Linked List is Empty")
        return self._head._element

    def last(self):
        if self.is_empty():
            raise Exception("Circularly Linked List is Empty")
        return self._tail._element

    def enqueue(self,e):
        newset=self._Node(e,None)
        if self.is_empty():
            self._head=newset
        else:
            self._tail._next=newset
        self._tail=newset
        self._head._next=newset
        self._size+=1
        
