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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack,result= [root],[]
        while stack:
            node = stack.pop()            
            result.append(node.val)            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

# Solution 2: Using Stack
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,result,curr=[],[],root
        while True:
            #Traversing to the leftmost node of the curr node
            if curr:
                #Add the node to the stack & result before going to its left child
                result.append(curr.val)
                stack.append(curr)
                curr=curr.left
            elif stack:
                #Backtrack from the empty subtree and visit the node at the top of the stack, if stack is empty we are done!
                curr=stack.pop()
                curr=curr.right
            else:
                return result
