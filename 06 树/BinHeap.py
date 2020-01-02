class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i//2 >0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i//2],self.heapList[i] = self.heapList[i],self.heapList[i//2]
            i = i//2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize +=1
        self.percUp(self.currentSize)
    
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i) #下沉选择更小的节点值
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i],self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = mc
    def minChild(self,i):
        if i*2 + 1 > self.currentSize: #仅有唯一子节点时
            return i*2
        else:#返回较小子节点
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i * 2
            else:
                return i*2 + 1
    def delMin(self):
        retval = self.heapList[i] #移走堆顶
        self.heapList[1] = self.heapList[currentSize]
        self.currentSize -=1
        self.heapList.pop()
        self.percDown(1) #新顶下沉
        return retval
    def buildHeap(self,alist):
        i = len(alist) // 2 #从叶节点的父节点开始
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList),i)
        while i>0 :
            print(self.heapList,i)
            self.percDown(i)
            i -=1
        print(self.heapList,i)

      