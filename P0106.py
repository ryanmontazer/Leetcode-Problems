# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        if len(inorder)==1:
            return TreeNode(inorder[0])
        base=postorder[-1]
        for i in range(0,len(inorder)):
            if inorder[i]==base:
                new_head=TreeNode(base)
                new_head.left=self.buildTree(inorder[0:i],postorder[0:i])
                new_head.right=self.buildTree(inorder[i+1:],postorder[i:-1])
                return new_head
