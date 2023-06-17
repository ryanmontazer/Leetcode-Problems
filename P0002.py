# Solution 1
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode(0)
        current=dummy_node
        carry=0
        while l1 or l2:
            val=carry
            if l1:
                val += l1.val
                l1= l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            carry,val= divmod(val,10)
            current.next=ListNode(val)
            current=current.next
        if carry:
            current.next=ListNode(carry)
        return dummy_node.next

# Solution 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        array_l1=[]
        array_l2=[]
        while l1 is not None:
            array_l1.append(l1.val)
            l1=l1.next
        l1_length=len(array_l1)
        while l2 is not None:
            array_l2.append(l2.val)
            l2=l2.next
        l2_length=len(array_l2)
        
        if l2_length>=l1_length:
            for i in range(0,l2_length-l1_length):
                array_l1.append(0)
        else:
            for i in range(0,l1_length-l2_length):
                array_l2.append(0)
        
        length=len(array_l1)
        
        reverse_l1=[]
        for i in range(0,length):
            reverse_l1.append(array_l1[length-1-i])
            
        reverse_l2=[]
        for i in range(0,length):
            reverse_l2.append(array_l2[length-1-i])
        
        head=ListNode(-1)
        curr=head
        temp=0
        
        for i in range(length-1,-1,-1):
            val=reverse_l1[i]+reverse_l2[i]+temp
            temp=(val- (val % 10))//10
            val= val % 10
            curr.next=ListNode(val)
            curr=curr.next
        if temp>0:
            curr.next=ListNode(1)
            curr.next.next=None
        else:
            curr.next=None
        
        return head.next
