# Solution 1: Using Stack
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
        if root is None:
            return
        stack1,stack2,result= [root],[],[]
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            for child in node.children:
                stack1.append(child)
        while stack2:
            node = stack2.pop()
            result.append(node.val)
        return result
        
# Solution 2: Using Stack
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
        result=[]
        if not root :
            return result
        stack=[[root,False]]
        while stack:
            node,visited= stack.pop()
            if visited:
                result.append(node.val)
            else:
                stack.append([node,True])
                for child in reversed(node.children):
                    stack.append([child,False])
        return result

# Solution 3: Using Recursion
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
