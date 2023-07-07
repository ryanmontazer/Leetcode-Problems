# Solution 1: using stack
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if not root :
            return result
        stack=[[root,False]]
        while stack:
            node,visited= stack.pop()
            if visited:
                result.append(node.val)
            else:
                stack.append([node,True])
                if node.right:
                    stack.append([node.right,False])
                if node.left:
                    stack.append([node.left,False])
        return result

# Solution 2: Recursion
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result= []
        if not root:
            return []
        if root.left:
            result= self.postorderTraversal(root.left) + result
        if root.right:
            result= result + self.postorderTraversal(root.right) 
        return result + [root.val]
