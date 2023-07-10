# Time: O(n)
# Space: O(log(n))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums :
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        i=len(nums)//2
        new_node=TreeNode(nums[i])
        new_node.left,new_node.right=self.sortedArrayToBST(nums[:i]),self.sortedArrayToBST(nums[i+1:])
        return new_node   
