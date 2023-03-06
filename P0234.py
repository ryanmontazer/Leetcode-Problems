# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ll_string=[]
        curr=head
        while curr is not None:
            ll_string.append(curr.val)
            curr=curr.next
        n=len(ll_string)
        for i in range(0,n//2):
            if ll_string[i] != ll_string[n-1-i]:
                return False
        return True
