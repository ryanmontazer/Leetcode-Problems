# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head=ListNode(0,head)
        old_head=dummy_head
        for i in range(left-1):
            old_head=old_head.next
        reversed_tail=old_head.next
        current=reversed_tail.next
        reversed_head=reversed_tail
        for i in range(right-left):
            new_current=current.next
            old_reversed_head=reversed_head
            reversed_head=current
            reversed_head.next=old_reversed_head
            current=new_current
        reversed_tail.next=current
        old_head.next=reversed_head
        return dummy_head.next
