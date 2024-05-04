# Time: O(n)
# Space: O(h+n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.leafValue(root1)==self.leafValue(root2)
    def leafValue(self,root1: Optional[TreeNode])-> list:
        if not root1:
            return []
        if not root1.left and not root1.right:
            return [root1.val]
        return self.leafValue(root1.left)+self.leafValue(root1.right)
