# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.pathIncluding(root,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)
    def pathIncluding(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        queue,result=[[root,root.val]],0
        while queue:
            element=queue.pop(0)
            result+=int(element[1]==targetSum)
            if element[0].left:
                queue.append([element[0].left,element[1]+element[0].left.val])
            if element[0].right:
                queue.append([element[0].right,element[1]+element[0].right.val])
        return result
