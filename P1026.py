# Time: O(n^2)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack,result=[root],0
        while stack:
            curr=stack.pop()
            #Traverse in all subtree of binary tree with root curr and update result each time
            stack1=[curr]
            while stack1:
                curr1=stack1.pop()
                result=max(result,abs(curr.val-curr1.val))
                if curr1.left:
                    stack1.append(curr1.left)
                if curr1.right:
                    stack1.append(curr1.right)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result
