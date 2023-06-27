# Time: O(n)
# Space: O(n)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        my_set, visited,  queue=set(), set() ,[[rooms[0],0]]
        visited.add(0)
        while queue:
            element= queue.pop(0)
            keys=element[0]
            visited.add(element[1])
            for key in keys:
                if key != 0 :
                    my_set.add(key)
                if not key in visited :
                    queue.append([rooms[key],key])
        if len(my_set)==len(rooms)-1:
            return True
        return False
