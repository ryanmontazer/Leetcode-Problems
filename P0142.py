# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes=set()
        while head is not None:
            if head in visited_nodes:
                return head
            visited_nodes.add(head)
            head=head.next
        return None
