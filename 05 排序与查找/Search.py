#查找——顺序查找
def SequentialSearch(alist, item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos +=1
    return found

#查找——有序查找
def orderSequentialSearch(alist,item):
    pos,found,stop = 0,False,False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos +=1
    return found 

#查找——二分查找
def BinarySearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) //2
        if alist[mid] == item:
            found = True
        else:
            if alist[mid] > item:
                last = mid - 1
            else:
                first = mid + 1
    return found

#查找——二分查找_递归版本
def BinarySearch_iter(alist,item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) //2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] > item:
                return BinarySearch_iter(alist[:mid],item)
            else:
                return BinarySearch_iter(alist[mid+1:],item)

temp=[0,1,2,3,5,6,9,10,12,18,20,24,30]
print(BinarySearch_iter(temp,5))
print(BinarySearch_iter(temp,8))
    






