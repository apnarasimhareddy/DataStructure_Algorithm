from double_linked_list import Double_Linked_List
class Linked_Dque(Double_Linked_List):
    def __init__(self):
        super().__init__()

    def first(self):
        if self.is_empty():
            raise Exception("Linked Dque is Empty")
        return self._head._next._element

    def last(self):
        if self.is_empty():
            raise Exception("Linked Dque is Empty")
        return self._tail._prev._element

    def first_add(self,v):
        return self.inseret_between(v,self._head,self._head._next)

    def last_add(self,v):
        return self.inseret_between(v,self._tail._prev,self._tail)

    def delete_first(self):
        if self.is_empty():
            raise Exception("Lined Dque is Empty")
        return self.delete_node(self._head._next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("Lnked dque is Empty")
        return self.delete_node(self._tail._prev)

l=Linked_Dque()
l.first_add(89)
l.last_add(78)
print(l.first())

