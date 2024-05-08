# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,pointer=ListNode(0),head
        prev.next=head
        while pointer and pointer.next:
            prev=prev.next
            pointer=pointer.next.next
        if prev.next:
            prev.next=prev.next.next
        if prev.val!=0:
            return head
        return None
