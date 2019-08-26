class Que:
    CAPACITY=10
    def __init__(self):
        self._data=[None]*Que.CAPACITY
        self._size=0
        self._front=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        anser=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        if 0<self._size<(len(self._data)//4):
            self._resize(len(self._data)//2)
        return anser

    def enqueue(self,e):
        if self._size==len(self._data):
            self._resize(2*len(self.data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1

    def _resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0

    def remove(self,index):
        if 0>index or index>self._size:
            raise ValueError('out of index')
        if index==self._size:
            self._data[index]=None
        for i in range(index,self._size):
            self._data[i]=self._data[i+1]
        self._data[self._size]=None
        self._size-=1

q=Que()
q.enqueue(34)
q.enqueue(23)
q.enqueue(45)
q.enqueue(12)
q.enqueue(67)
q.enqueue(89)
print(q._data)
print(q._size)
q.remove(3)
print(q._data)

