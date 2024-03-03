Solution 1:
# Time: O(n)
# Space: O(1)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows=1
        x_max=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]>x_max:
                arrows+=1
                x_max=points[i][1]
            else:
                x_max=min(x_max,points[i][1])
        return arrows

Solution 2:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        return self.helper(points)
    def helper(self,points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        x_max,index=points[0][1],0
        for i in range(1,len(points)):
            if points[i][0]>x_max:
                break
            x_max,index=min(x_max,points[i][1]),i
        return 1+self.helper(points[index+1:])

Solution 3:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        points.sort()
        x_max,index=points[0][1],0
        for i in range(1,len(points)):
            if points[i][0]>x_max:
                break
            x_max,index=min(x_max,points[i][1]),i
        return 1+self.findMinArrowShots(points[index+1:])
