# Time O(n)
# Space O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        while curr:
            if curr.child:
                if curr.next:
                    the_most_next=curr.child
                    while the_most_next.next:
                        the_most_next=the_most_next.next
                    the_most_next.next=curr.next
                    the_most_next.next.prev=the_most_next
                curr.next=curr.child
                curr.next.prev=curr
                curr.child=None
            curr=curr.next
        return head
