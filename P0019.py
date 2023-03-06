# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr is not None:
            curr=curr.next
            length+=1
        curr=head
        for i in range(1,length-n):
            curr=curr.next
        if curr.next is None:
            return None
        if length==n:
            head=head.next
            return head
        curr.next=curr.next.next
        return head
