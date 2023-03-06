# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        if head is None:
            return head
        curr=head.next
        head.next=None
        while curr is not None:
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node
        head=prev
        return head
