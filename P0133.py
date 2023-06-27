# Time: O(n)
# Space: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #visited is a dictionary which will contain all the original nodes as the key and will create the corresponding node in deep copy as the value
        queue, visited= [node], {}
        if not node:
            return None
        while queue:
            original_node=queue.pop()
            visited[original_node]=Node(original_node.val)
            for neighbor in original_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
        #Now we will make neighbors for all elements in the visited.values()
        for original_node, new_node in visited.items():
            for neighbor in original_node.neighbors:
                new_node.neighbors.append(visited[neighbor])
        return visited[node]
