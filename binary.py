def binary_search(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        elif target>data[mid]:
            return binary_search(data,target,mid-1,high)
data=[0,1,2,3,4,5,6,7]
high=len(data)
print(binary_search(data,5,0,high))



