Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        array,result=self.arrayBST(root),float('inf')
        if len(array)<2:
            return 0
        for i in range(1,len(array)):
            result=int(min(result,array[i]-array[i-1]))
        return result
    def arrayBST(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []
        return self.arrayBST(root.left)+[root.val]+self.arrayBST(root.right)
        
Solution 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        return int(self.newGetMinimumDifference(root))
    def newGetMinimumDifference (self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return float('inf')
        if not root.left:
            element=root.right
            while element.left:
                element=element.left
            return min(element.val-root.val,root.right.val-root.val,self.newGetMinimumDifference(root.right))
        if not root.right:
            element=root.left
            while element.right:
                element=element.right
            return min(root.val-element.val,self.newGetMinimumDifference(root.left))
        if root.left and root.right:
            element=root.left
            while element.right:
                element=element.right
            element1=root.right
            while element1.left:
                element1=element1.left
            return min(element1.val-root.val,root.val-element.val,self.newGetMinimumDifference(root.left),self.newGetMinimumDifference(root.right),root.val-root.left.val,root.right.val-root.val)
