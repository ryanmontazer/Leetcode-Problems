# Time: O(h)
# Space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr,new_node=root,TreeNode(val)
        if not root:
            return new_node
        while True:
            if curr.val<val and not curr.right:
                curr.right=new_node
                return root
            elif curr.val>val and not curr.left:
                curr.left=new_node
                return root
            elif curr.val<val:
                curr=curr.right
            else:
                curr=curr.left
