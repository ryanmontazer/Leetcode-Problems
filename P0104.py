# Solution1:
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))

# Solution2:
# Time: O(n)
# Space: O(w)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        result=0
        stack=deque([root])
        while stack:
            for i in range(len(stack)):
                element=stack.popleft()
                if element.left:
                    stack.append(element.left)
                if element.right:
                    stack.append(element.right)
            result+=1
        return result

# Solution 3:
# Time: O(n)
# Space: O(w)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack=[[root,1]]
        result=1
        while stack:
            element,level=stack.pop(0)
            if element.left: stack.append([element.left,level+1])
            if element.right: stack.append([element.right,level+1])
            result=max(result,level)
        return result
