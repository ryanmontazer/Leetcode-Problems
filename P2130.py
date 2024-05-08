Solution 2
# Time: O(n)
# Space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr,array=head,[]
        while curr:
            array.append(curr.val)
            curr=curr.next
        left,right,maximum=0,len(array)-1,float("-inf")
        while left<right:
            maximum=max(maximum,array[left]+array[right])
            left+=1
            right-=1
        return maximum  
