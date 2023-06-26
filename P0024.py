# Solution 1
# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last_node, curr =ListNode(0), head
        return_head=last_node
        while curr and curr.next:
            last_node.next=curr.next
            #swap curr and curr.next, update last_node and move curr two steps ahead
            new_curr=curr.next.next
            curr.next.next, curr.next, last_node =curr, new_curr, curr
            curr=new_curr
        if curr:
            last_node.next=curr
        return return_head.next

# Solution 2
# Time: O(n)
# Space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head, new_head.next, head.next =head.next, head, self.swapPairs(head.next.next)
        return new_head
