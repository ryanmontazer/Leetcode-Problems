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
