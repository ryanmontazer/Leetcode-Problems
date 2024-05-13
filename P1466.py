# Time: O(connections)
# Space: O(n)
class ListNode:
    def __init__(self, val=0, child=None):
        self.val = val
        self.child = [] if child is None else child
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph,visited=[],set()
        for i in range(n):
            graph.append(ListNode(i))
        for i,j in connections:
            graph[i].child.append([graph[j],1])
            graph[j].child.append([graph[i],-1])
        array,result=[graph[0]],0
        while array:
            element=array.pop(0)
            visited.add(element.val)
            for child in element.child:
                if child[0].val not in visited:
                    array.append(child[0])
                    if child[1]==1:
                        result+=1
        return result
