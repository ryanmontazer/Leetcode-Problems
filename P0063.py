# Time: O(mn)
# Space: O(1)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obstacleGrid[0][0]=(int(obstacleGrid[0][0]==1)-1)*(obstacleGrid[0][0]-1)
        for i in range(1,len(obstacleGrid)):
            obstacleGrid[i][0]=(1-int(obstacleGrid[i][0]==1))*obstacleGrid[i-1][0]
        for i in range(1,len(obstacleGrid[0])):
            obstacleGrid[0][i]=(1-int(obstacleGrid[0][i]==1))*obstacleGrid[0][i-1]
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
               obstacleGrid[i][j]=(1-obstacleGrid[i][j])*(obstacleGrid[i-1][j]+obstacleGrid[i][j-1])    
        return obstacleGrid[-1][-1]
