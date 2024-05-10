# Time: O(n^2)
# Space: O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        result,remaining_cities=0,[0]*len(isConnected)
        for i in range(len(isConnected)):
            remaining_cities[i]=i
        while remaining_cities:
            result+=1
            queue=[remaining_cities.pop()]
            while queue:
                element=queue.pop()
                if element in remaining_cities:
                    remaining_cities.remove(element)
                for city in remaining_cities:
                    if isConnected[element][city]==1:
                        queue.append(city)
        return result
