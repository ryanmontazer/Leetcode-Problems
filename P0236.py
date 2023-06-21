# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root is p or root is q:
            return root
        lca_left=self.lowestCommonAncestor(root.left, p, q)
        lca_right=self.lowestCommonAncestor(root.right, p, q)
        if lca_left and lca_right:
            return root
        else:
            return lca_left or lca_right
