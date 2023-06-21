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
    def connect(self, root: 'Node') -> 'Node':
        #level_pointer is the first non empty node of the current level
        level_pointer= root
        while level_pointer:
            #level_pointer1 traverse in the same level of level_pointer 
            level_pointer1=level_pointer
            #Assign level_pointer2 to the first Node of next level and set curr=level_pointer2
            level_pointer2, new_pointer=None, level_pointer
            while new_pointer and not level_pointer2:
                if new_pointer.left or new_pointer.right:
                    level_pointer2=new_pointer.left or new_pointer.right
                else:
                    new_pointer=new_pointer.next
            curr=level_pointer2
            #Traverse curr through the same level
            while curr and level_pointer1:
                #Assign curr.next
                curr_next=None
                while not curr_next and level_pointer1:
                    if curr is level_pointer1.left:
                        curr_next=level_pointer1.right
                    if not curr_next and curr is not (level_pointer1.left or level_pointer1.right):
                        curr_next=level_pointer1.left or level_pointer1.right
                    if not curr_next:
                        level_pointer1=level_pointer1.next 
                curr.next=curr_next
                curr=curr.next
                #Update level_pointer1
                if level_pointer1 and curr is level_pointer1.right:
                    level_pointer1=level_pointer1.next
            #Update level_pointer by moving it to the next level
            level_pointer=level_pointer2
        return root
