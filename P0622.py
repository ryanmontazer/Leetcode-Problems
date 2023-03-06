class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.queue=[0]*k
        self.head=-1
        self.tail=-1

    def enQueue(self, value: int) -> bool:
        new_tail=(self.tail+1) % self.k
        if self.head==new_tail:
            return False
        elif self.head==-1:
            self.head=0
            self.tail=0
            self.queue[0]=value
            return True
        else:
            self.tail=new_tail
            self.queue[new_tail]=value
            return True

    def deQueue(self) -> bool:
        if self.head==-1:
            return False
        elif self.head==self.tail:
            self.head=-1
            self.tail=-1
            return True
        else:
            self.head=(self.head+1) % self.k
            return True

    def Front(self) -> int:
        if self.head==-1:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.head==-1:
            return -1
        return self.queue[self.tail]
    
    def isEmpty(self) -> bool:
        if self.head==-1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.tail+1) % self.k==self.head:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
