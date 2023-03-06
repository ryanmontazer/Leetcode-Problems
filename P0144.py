# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        result=[]
        current=root
        while True:
            if current:
                result.append(current.val)
                stack.append(current)
                current=current.left
            elif stack:
                current=stack.pop()
                current=current.right
            else:
                break
        return result
