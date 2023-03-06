class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
        
class MyLinkedList:

    def __init__(self):
        self.head=ListNode(None)
        self.size=0

    def get(self, index: int) -> int:
        if index<0 or index>self.size-1:
            return -1
        curr=self.head
        for i in range(0,index):
            curr=curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.size+=1
        curr=ListNode(val)
        curr.next=self.head
        self.head=curr
        
    def addAtTail(self, val: int) -> None:
        if self.size==0:
            self.head=ListNode(val)
            self.size+=1
            return        
        curr=self.head
        for i in range(1,self.size):
            curr=curr.next
        curr.next=ListNode(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index > self.size:
            return
        new_node= ListNode(val)
        prev=self.head
        curr=prev.next
        if index==0:
            new_node.next=self.head
            self.head=new_node
            self.size+=1
            return
        for i in range(1,index):
            prev=prev.next
            curr=curr.next
        new_node.next=curr
        prev.next=new_node
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index > self.size-1:
            return
        prev=self.head
        curr=prev.next
        if index==0:
            self.head=self.head.next
            self.size-=1
            return
        for i in range(1,index):
            prev=prev.next
            curr=curr.next
        prev.next=curr.next
        self.size-=1

            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
