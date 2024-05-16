# Time: O(n)
# Space: O(1)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        delx,dely=coordinates[0][0]-coordinates[1][0],coordinates[0][1]-coordinates[1][1]
        for i in range(2,len(coordinates)):
            if (coordinates[i][1]-coordinates[0][1])*delx!=dely*(coordinates[i][0]-coordinates[0][0]):
                return False
        return True
