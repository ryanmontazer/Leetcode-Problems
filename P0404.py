# Time: O(n)
# Space: O(w)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        summation,queue=0,[root]
        while queue:
            element=queue.pop(0)
            if element.left:
                queue.append(element.left)
                if not (element.left.left or element.left.right):
                    summation+=element.left.val
            if element.right:
                queue.append(element.right)
        return summation
