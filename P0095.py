# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTreesWithNumbers(1,n)
    def generateTreesWithNumbers(self, i:int, j:int) -> List[Optional[TreeNode]]:
        if j<i:
            return [None]
        result=[]
        for val in range(i,j+1):
            bts1=self.generateTreesWithNumbers(i,val-1)
            bts2=self.generateTreesWithNumbers(val+1,j)
            for item1 in bts1:
                for item2 in bts2:
                    result.append(TreeNode(val,item1,item2))
        return result
