# Solution 1
# Time O(n)
# Space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr, par1_head, par2_head= head, ListNode(0), ListNode(0)
        curr_par1, curr_par2= par1_head, par2_head
        while curr:
            #Assigning curr to either par1 or par2
            if curr.val<x:
                curr_par1.next=curr
                curr_par1=curr_par1.next
            else:
                curr_par2.next=curr
                curr_par2=curr_par2.next
            curr=curr.next
        curr_par1.next=par2_head.next
        curr_par2.next=None
        return par1_head.next


# Solution 2
# Time O(n)
# Space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #Initializing head1 and head2
        curr, head1, head2, check= head, None, None, 0
        while curr and check<2:
            if curr.val<x and not head1:
                head1=curr
                check+=1
            if curr.val>=x and not head2:
                head2=curr
                check+=1
            curr=curr.next
        #Bulding two sub linked lists 
        curr, end1, end2=head, head1, head2
        while curr:
            if curr.val<x and curr is not head1:
                end1.next=curr
                end1=end1.next
            if curr.val>=x and curr is not head2:
                end2.next=curr
                end2=end2.next
            curr=curr.next
        if end2:
            end2.next=None
        #Joining the linked lists together
        if end1:
            end1.next=head2
            return head1
        return head2
