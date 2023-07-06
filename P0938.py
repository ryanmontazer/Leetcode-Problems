# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result, stack=0,[root]
        while stack:
            curr=stack.pop()
            if curr.val>=low and curr.val<=high:
                result+=curr.val
            if curr.left and curr.val>low:
                stack.append(curr.left)
            if curr.right and curr.val<high:
                stack.append(curr.right)
        return result
