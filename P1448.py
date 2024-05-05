Solution 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        array,array_max=[],[]
        queue=[root]
        while queue:
            element=queue.pop()
            array.append(element.val)
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)
        queue_max=[root]
        while queue_max:
            element=queue_max.pop()
            array_max.append(element.val)
            if element.left:
                element.left.val=max(element.val,element.left.val)
                queue_max.append(element.left)
            if element.right:
                element.right.val=max(element.val,element.right.val)
                queue_max.append(element.right)
        result=0
        for i in range(len(array)):
            if array_max[i]<=array[i]:
                result+=1
        return result
