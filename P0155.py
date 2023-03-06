class MinStack:

    def __init__(self):
        self.stack=[]
        self.tail=-1

    def push(self, val: int) -> None:
        self.tail=self.tail+1        
        self.stack.insert(self.tail,val)

    def pop(self) -> None:
        self.tail=self.tail-1

    def top(self) -> int:
        return self.stack[self.tail]

    def getMin(self) -> int:
        stack_min=min(self.stack[0:self.tail+1])
        return stack_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
