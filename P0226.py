# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.subInvert(root)
        return root
    def subInvert(self,root):
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.subInvert(root.left)
        self.subInvert(root.right)
