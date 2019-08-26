import ctypes
class DynamicArray:
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)

    def len(self):
        return self._n

    def __getitem__(self,k):
        if not 0<=k<self._n:
            raise IndexError(" Invalid index")
        return self._A[k]
    def append(self,obj):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1

    def _resize(self,c):
        B=self._make_array(c)
        for k in range(self._n):
            B[k]=self._A[k]
        self._A=B
        self._capacity=c

    def _make_array(self,c):
        return (c*ctypes.py_object)()
    def insert(self,k,v):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n,k,-1):
            self._A[j]=self._A[j-1]
        self._A[k]=v
        self._n+=1
da=DynamicArray()
da.append(2)
da.append(3)
da.insert(0,4)
print(da.len())
print(da._capacity)
import sys
print(sys.getsizeof(da))
from time import time
def contain():
    start=time()
    data=[]
    for i in range(100000):
        data.append(i)
    print(sys.getsizeof(data))
    if 5 in data:
        print('5')
    end=time()
    return end-start

print(contain())


