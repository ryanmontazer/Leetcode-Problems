# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def linearing (root: Optional[TreeNode]) -> list:
            if not root:
                return []
            return linearing(root.left)+[root.val]+linearing(root.right)
        return linearing(root)[k-1]
