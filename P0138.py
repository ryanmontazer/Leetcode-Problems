# Time O(n)
# Space O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #inserting identical nodes in between the original nodes
        current=head
        while current:
            current_next=current.next
            new_node=Node(current.val)
            current.next=new_node
            new_node.next=current_next
            current=current_next
        #updating new nodes with their randoms
        current=head
        while current:
            if current.random:
                current.next.random=current.random.next
            else:
                current.next.random=None
            current=current.next.next
        #separating the new set of nodes from the original ones
        current=head
        if head:
            head_next=head.next
        while current:
            current_original_next=current.next.next
            if current.next.next:
                current.next.next=current.next.next.next
                current.next=current_original_next
            else:
                current.next.next=None
            current=current_original_next
        if head:
            return head_next
        return None
