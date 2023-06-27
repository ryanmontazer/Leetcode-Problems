# Time: O(n)
# Space: O(n)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited,  queue= {0} ,[[rooms[0],0]]
        while queue:
            element= queue.pop(0)
            keys=element[0]
            visited.add(element[1])
            for key in keys:
                if not key in visited :
                    queue.append([rooms[key],key])
        if len(visited)==len(rooms):
            return True
        return False
