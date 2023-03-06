# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail=head
        length=1
        while True:
            if tail.next:
                tail=tail.next
                length+=1
            else:
                break
        k=(length-k) % length
        new_head=head
        new_tail=tail
        for i in range(0,k):
            if i==k-1:
                new_tail=new_head
            new_head=new_head.next
        
        tail.next=head
        head=new_head
        new_tail.next=None
        return head
