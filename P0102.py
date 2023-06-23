# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result, queue =[], [[root,1]]
        while queue:
            curr=queue.pop(0)
            level=curr[1]
            if curr[0].left:
                queue.append([curr[0].left,level+1])
            if curr[0].right:
                queue.append([curr[0].right,level+1])
            if level-len(result):
                result.append([curr[0].val])
            else:
                result[-1].append(curr[0].val)
        return result
