# Solution 1:
# Time: O(m+n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(l1: Optional[ListNode]) -> Optional[ListNode]:
            prev,curr=None,l1
            while curr:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            return prev
        l1,l2=reverse(l1),reverse(l2)
        dummy=ListNode(0)
        l3,result=dummy,0
        while l1 or l2 or result:
            if l1:
                result+=l1.val
                l1=l1.next
            if l2:
                result+=l2.val
                l2=l2.next
            l3.next=ListNode(result%10)
            l3=l3.next
            result=result//10
        return reverse(dummy.next)

# Solution 2:
# Time: O(m+n)
# Space: O(m+n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        head=l1
        while head:
            list1.append(head.val)
            head=head.next
        list2=[]
        head=l2
        while head:
            list2.append(head.val)
            head=head.next
        list3=[]
        result=0
        for i in range(max(len(list1),len(list2))):
            if i<len(list1):
                result+=list1[-i-1]
            if i<len(list2):
                result+=list2[-i-1]
            list3.append(result%10)
            result=result//10
        if result:
            list3.append(result)
        dummy=ListNode(0)
        head=dummy
        for i in range(len(list3)):
            head.next=ListNode(list3[-i-1])
            head=head.next
        return dummy.next
