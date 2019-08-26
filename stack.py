class ArrayStack:
    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def push(self,v):
        self._data.append(v)
    def is_empty(self):
        return len(self._data)==0
    def pop(slef):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()
    def top(self):
        if self.is_empty():
            raise Empty('stak is empty')
        return self._data[-1]

    def is_matched(self,exp):
        left='([{'
        right=')]}'
        for c in exp:
            if c in left:
                self.push(c)
            elif c in right:
                if self.is_empty():
                    return False
                if right.index(c)!=left.index(self._data.pop()):
                    return False
        return self.is_empty()


s=ArrayStack()
print(s.is_empty())
print(s.is_matched('{2+3[4(3-2)]}'))

