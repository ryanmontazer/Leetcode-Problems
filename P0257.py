# Time: O(nh)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]
        result=[]
        if root.left:
            for element in self.binaryTreePaths(root.left):
                result.append(str(root.val)+"->"+element)
        if root.right:
            for element in self.binaryTreePaths(root.right):
                result.append(str(root.val)+"->"+element)
        return result
