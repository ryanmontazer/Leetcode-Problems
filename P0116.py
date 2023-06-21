# Time O(n)
# Space O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root :
            return root
        level_pointer=root
        while level_pointer:
            level_pointer1, curr=level_pointer, level_pointer.left
            while curr:
                #Assigning next of the current node
                if curr is level_pointer1.left:
                    curr.next=level_pointer1.right
                elif level_pointer1.next:
                    curr.next=level_pointer1.next.left
                    level_pointer1=level_pointer1.next
                curr=curr.next
            level_pointer=level_pointer.left
        return root
