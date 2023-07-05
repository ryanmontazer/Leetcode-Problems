# Time: O(n)
# Space: O(w)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        #Result is defind in such a way that result[-1] is the depth of last element
        queue,result=[[root,1]],[-1]
        while queue:
            curr, depth= queue.pop(0)
            if result[-1]==depth:
                result[-2].append(curr.val)
            else:
                result.pop()
                result.append([curr.val])
                result.append(depth)
            for child in curr.children:
                queue.append([child,depth+1])
        result.pop()
        return result
