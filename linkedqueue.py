class LinkedQueue:

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

    def enqueue(self,e):
        newset=self._Node(e,None)
        if self._size==0:
            self._head=newset
        else:
            self._tail._next=newset
        self._tail=newset
        self._size+=1

    def dequeue(self):
        if self.is_empty():
            raise Empty('LinkedQueue is Empty')
        answer=self._head._element
        self._head=self._head._next
        self._size-=1
        if self.is_empty():
            self._tail=None
        return answer

    def first(self):
        if self.is_empty():
            raise Empty("LinkedQueue is Empty")
        return self._head._element

    def last(self):
        if self.is_empty():
            raise Empty("LinkedQueue is Empty")
        return self._tail._element

l=LinkedQueue()
l.enqueue(3)
l.enqueue(4)
l.enqueue(5)
l.enqueue(6)
l.dequeue()
print(l.first())
print(l.last())