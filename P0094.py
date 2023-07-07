# Solution 1: Using Stack
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,result,curr=[],[],root
        while True:
            #Traverse to the leftmost node of the curr node
            if curr:
                #Add the node to the stack before going to its left child
                stack.append(curr)
                curr=curr.left
            #Backtrack from the empty subtree and visit the node at the top of the stack, if stack is empty we are done!
            elif stack:
                curr=stack.pop()
                result.append(curr.val)
                curr=curr.right
            else:
                return result

# Solution 2 : Using Recursion
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
