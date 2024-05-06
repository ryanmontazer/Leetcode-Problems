# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import statistics
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue,array,pre_index,result=[[root,1]],[],1,[]
        while queue:
            element=queue.pop(0)
            index=element[1]
            if element[0].left:
                queue.append([element[0].left,index+1])
            if element[0].right:
                queue.append([element[0].right,index+1])
            if not array:
                array.append([element[0].val])
            elif pre_index==index:
                array[-1].append(element[0].val)
            else:
                pre_index=index
                array.append([element[0].val])
        for element in array:
            result.append(statistics.mean(element))
        return result
