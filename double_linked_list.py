class Double_Linked_List:
    class _Node:
        def __init__(self,prev,element,next):
            self._prev=prev
            self._element=element
            self._next=next
    def __init__(self):
        self._head=self._Node(None,None,None)
        self._tail=self._Node(None,None,None)
        self._head._next=self._tail
        self._tail._prev=self._head
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def inseret_between(self,v,prodecesor,successor):
        newset=self._Node(prodecesor,v,successor)
        prodecesor._next=newset
        successor._prev=newset
        self._size+=1

    def delete_node(self,node):
        prodecesor=node._prev
        successor=node._next
        prodecesor._next=successor
        successor._prev=prodecesor
        self._size-=1
        element=node._element
        node._next=node._prev=node._element=None
        return element
