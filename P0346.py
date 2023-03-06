class MovingAverage:

    def __init__(self, size: int):
        self.size=size
        self.count=0
        self.sum=0
        self.queue=[0.1]*size
        self.head=-1
        self.tail=-1

    def next(self, val: int) -> float:
        if self.count<self.size: #In this case just add the element at tail
            self.head=0
            self.tail=self.count
            self.queue[self.tail]=val
            self.count+=1
            self.sum+=val
            return self.sum/self.count
        else:
            self.sum=self.sum+val-self.queue[self.head]
            self.head=(self.head+1) % self.size
            self.tail=(self.tail+1) % self.size
            self.queue[self.tail]=val
            return self.sum/self.size
            
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
