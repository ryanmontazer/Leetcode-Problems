# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head=ListNode(float("inf"),head)
        prev,curr=new_head,head
        while curr:
            count=0
            while curr.next and curr.next.val==curr.val:
                count=1
                curr=curr.next
            if count==1:
                prev.next=curr.next
                curr=curr.next
            else:
                prev,curr=curr,curr.next
        return new_head.next
