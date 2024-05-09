# Time: O(n)
# Space: O(w)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=[[root,1]]
        result=[1,root.val]
        curr=[0,-abs(root.val)-1]
        while queue:
            element=queue.pop(0)
            if element[0].left:
                queue.append([element[0].left,element[1]+1])
            if element[0].right:
                queue.append([element[0].right,element[1]+1])
            if element[1]==curr[0]:
                curr[1]+=element[0].val
            else:
                if curr[1]>result[1]:
                    result=curr
                curr=[element[1],element[0].val]
        if curr[1]>result[1]:
            return curr[0]
        return result[0]   
