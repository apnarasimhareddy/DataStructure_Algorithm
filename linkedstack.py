class LinkedStack:
    class _Node:
        __slots__='_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next

    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def push(self,e):
        self._head=self._Node(e,self._head)
        self._size+=1
    def is_empty(self):
        return self._size==0
    def pop(self):
        if self.is_empty():
            raise Empty("LinkedStack is empty")
        answer=self._head._element
        self._head=self._head._next
        self._size-=1
        return answer
    def top(self):
        if self.is_empty():
            raise Empty('LinkedStack is Empty')
        return self._head._element

l=LinkedStack()
l.push(0)
l.push(1)
l.push(2)
l.pop()
l.pop()
l.pop()
l.top()
print(l.pop())