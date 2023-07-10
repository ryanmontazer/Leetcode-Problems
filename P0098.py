# Solution 1: Recursion
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.findMax(root.left)>=root.val:
            return False
        if self.findMin(root.right)<=root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    def findMax(self,root)->float:
        stack,result=[root],float("-inf")
        if not root:
            return result
        while stack:
            curr=stack.pop()
            if curr.val>result:
                result=curr.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result
    def findMin(self,root)->float:
        stack,result=[root],float("inf")
        if not root:
            return result
        while stack:
            curr=stack.pop()
            if curr.val<result:
                result=curr.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result
