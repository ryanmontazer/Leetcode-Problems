# Solution 1: Iterative & Queue
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.right is None
        if root.right is None:
            return root.left is None
        queue=[root.left, root.right]
        while queue:
            queue_left_graph,queue_right_graph = queue.pop(0), queue.pop(0)
            if queue_left_graph.val != queue_right_graph.val:
                return False
            if queue_left_graph.left:
                if not queue_right_graph.right:
                    return False
                if queue_left_graph.left.val != queue_right_graph.right.val:
                    return False
                queue.extend([queue_left_graph.left,queue_right_graph.right])
            if not queue_left_graph.left and queue_right_graph.right:
                return False
            if queue_left_graph.right:
                if not queue_right_graph.left:
                    return False
                if queue_left_graph.right.val != queue_right_graph.left.val:
                    return False
                queue.extend([queue_left_graph.right,queue_right_graph.left])
            if not queue_left_graph.right and queue_right_graph.left:
                return False
        return True
        
# Solution 2: Recursion
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.right is None
        if root.right is None:
            return root.left is None
        if root.left.val != root.right.val:
            return False
        new_node1= TreeNode(0)
        new_node1.left, new_node1.right = root.left.left, root.right.right
        new_node2= TreeNode(0)
        new_node2.left, new_node2.right= root.left.right, root.right.left
        return self.isSymmetric(new_node1) and self.isSymmetric(new_node2)
