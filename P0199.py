# Time: O(n)
# Space: O(w)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue,level,result=[[root,1]],1,[]
        prev,curr=float("-inf"),float("-inf")
        while queue:
            element=queue.pop(0)
            prev,curr=curr,element[0].val
            if element[1]>level:
                level=element[1]
                result.append(prev)
            if element[0].left:
                queue.append([element[0].left,element[1]+1])
            if element[0].right:
                queue.append([element[0].right,element[1]+1])
        result.append(curr)
        return result
