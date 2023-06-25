# Solution 1
# Time: O(h)
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr=root
        while curr:
            if not curr.val-val:
                return curr
            elif curr.val>val:
                curr=curr.left
            elif curr.val<val:
                curr=curr.right
        return curr

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
