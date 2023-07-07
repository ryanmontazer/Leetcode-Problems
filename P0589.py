# Solution 2: Recursion
# Time: O(n)
# Space: O(h)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result=[]
        if not root:
            return result
        if not root.children:
            return [root.val]
        result.append(root.val)
        for child in root.children:
            result=result+self.preorder(child)
        return result
