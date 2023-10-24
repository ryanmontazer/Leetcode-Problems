class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0][0]==points[1][0] and points[0][1]==points[1][1]:
            return False
        if points[0][0]==points[2][0] and points[0][1]==points[2][1]:
            return False
        if points[2][0]==points[1][0] and points[2][1]==points[1][1]:
            return False
        if (points[0][1]-points[1][1])*(points[0][1]-points[2][1])==0:
            if points[0][1]==points[1][1] and points[0][1]==points[2][1]:
                return False
            else:
                return True
        if (points[0][0]-points[1][0])/(points[0][1]-points[1][1]) != (points[0][0]-points[2][0])/(points[0][1]-points[2][1]):
            return True
        else:
            return False
