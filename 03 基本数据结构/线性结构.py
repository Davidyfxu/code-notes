#线性结构
#栈 LIFO
class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)

#队列 FIFO
class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

#双端队列
class Deque():
    def __init__(self):
        self.items = []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        self.items.pop()
    def removeRear(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

#链表实现：节点Node
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
#链表实现：无序表UnorderedList
class UnorderedList:
    def __init__(self):
        self.head = None
    def add(self,item): 
        #添加新数据项最快捷的位置是表头， 整个链表的首位置。
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        #从链条头head开始遍历到表尾同 
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False 
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

#链表实现：有序表
class OrderedList:
    def __init__(self):
        self.head = None
    def add(self,item): 
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
    def size(self):
        #从链条头head开始遍历到表尾同 
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count
    def search(self,item):
        current = self.head
        found = False 
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())