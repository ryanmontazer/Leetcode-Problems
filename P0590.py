# Recursive Solution
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        result=[]
        for child in root.children:
            result=result+self.postorder(child)
        result=result+[root.val]
        return result
