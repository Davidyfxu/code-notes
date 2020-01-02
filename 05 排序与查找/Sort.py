#冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0 , -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]

#冒泡排序——短冒泡
def shortbubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum >0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i],alist[i+1] = alist[i+1],alist[i]
        passnum -=1

#选择排序
def selectionSort(alist):
    for passnum in range(len(alist)-1 , 0 ,-1):
        positionOfMax = 0
        for location in range(passnum+1): #注意这个 passnum+1 项,不能丢
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[passnum],alist[positionOfMax] = alist[positionOfMax],alist[location] 

#插入排序
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index]
        position = index
        
        #挪项插入
        while position > 0 and  alist[position-1] > currentValue:
            alist[position] = alist[position - 1]
            position -=1
        alist[position] = currentValue 

#希尔排序  --记得不够牢
def shellSort(alist):
    sublistcount = len(alist) //2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        
        print(sublistcount,alist)

        sublistcount = sublistcount //2

def gapInsertionSort(alist,start,gap):
    for index in range(start+gap,len(alist),gap):
        currentValue = alist[index]
        position = index
        while position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position -=gap
        alist[position] = currentValue

#归并排序 pythonic版
def merge_Sort(alist):
    if len(alist) <= 1:
        return alist
    
    mid = len(alist) //2
    left = merge_Sort(alist[:mid])
    right = merge_Sort(alist[mid:])
    
    merged = []
    while left and right:
        if left[0] > right[0]:
            merged.append(right.pop(0))
        else:
            merged.append(left.pop(0))
    merged.extend(right if right else left)
    return merged

#归并排序 
def mergeSort(alist):
    if len(alist) >1:
        mid = len(alist) //2
        left = alist[:mid]
        right = alist[mid:]
    
        mergeSort(left)
        mergeSort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] > right[j]:
                alist[k] = right[j]
                j +=1
            else:
                alist[k] = left[i]
                i +=1
            k +=1
        while i<len(left):
            alist[k] = left[i]
            i +=1
            k +=1
        while j<len(right):
            alist[k] = right[j]
            j +=1
            k +=1

#快速排序
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first<last:
        splitposition = partition(alist,first,last)
        quickSortHelper(alist,first,splitposition-1)
        quickSortHelper(alist,splitposition+1,last)
def partition(alist,first,last):
    pivotvalue = alist[first]
    left = first+1
    right = last
    done = False
    while not done:
        while left <= right and pivotvalue > alist[left]:
            left +=1
        while left <= right and pivotvalue < alist[right]:
            right -=1
        if right < left :
            done = True
        else:
            alist[left],alist[right] = alist[right],alist[left]
    
    alist[first],alist[right] = alist[right],alist[first]
    return right

temp = [54,26,93,17,77,31,44,55,20]
mergeSort(temp)
print(temp)