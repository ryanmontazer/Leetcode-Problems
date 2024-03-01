# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0)
    def helper(self, root: Optional[TreeNode], carry: int) -> int:
        curr,par=root, None
        queue=[[curr,par]]
        while queue:
            curr,par=queue.pop()
            if curr.val>1:
                curr.val-=1
                if self.validation(curr.left)<0:
                    curr.left.val+=1
                    return self.helper(root,carry+1)
                elif self.validation(curr.right)<0:
                    curr.right.val+=1
                    return self.helper(root,carry+1)
                else :
                    par.val+=1
                    return self.helper(root,carry+1)
            if curr.left:
                queue.append([curr.left,curr])
            if curr.right:
                queue.append([curr.right,curr]) 
        # if no element has value >1 , return carry
        return carry
    def validation(self, root: Optional[TreeNode])-> int:
    # returns all coins in root1 and childs minus all nodes
    # if returns negative, we need more coin for this branch 
        if not root:
            return 0
        result=root.val-1
        if root.left:
            result+=self.validation(root.left)
        if root.right:
            result+=self.validation(root.right)
        return result
