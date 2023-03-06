# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        ll_tail=head
        while ll_tail.next is not None:
            ll_tail=ll_tail.next
        ll_tail_new=ll_tail
        prev=head
        curr=head.next
        while True:
            if prev is ll_tail:
                return head
            elif curr is ll_tail:
                prev.next=ll_tail.next
                ll_tail_new.next=curr
                ll_tail_new=curr
                ll_tail_new.next=None
                return head
            else:
                prev_update=curr.next
                curr_update=curr.next.next
                prev.next=curr.next
                ll_tail_new.next=curr
                ll_tail_new=curr
                ll_tail_new.next=None
                prev=prev_update
                curr=curr_update
