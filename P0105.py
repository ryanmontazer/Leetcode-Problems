# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        head=preorder[0]
        new_node=TreeNode(head)
        for i in range(len(preorder)):
            if inorder[i]==head:
                new_node.left=self.buildTree(preorder[1:i+1],inorder[0:i])
                new_node.right=self.buildTree(preorder[i+1:],inorder[i+1:])
                return new_node
