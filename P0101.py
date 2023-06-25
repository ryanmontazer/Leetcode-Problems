# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.right is None
        if root.right is None:
            return root.left is None
        if root.left.val != root.right.val:
            return False
        new_node1= TreeNode(0)
        new_node1.left, new_node1.right = root.left.left, root.right.right
        new_node2= TreeNode(0)
        new_node2.left, new_node2.right= root.left.right, root.right.left
        return self.isSymmetric(new_node1) and self.isSymmetric(new_node2)
