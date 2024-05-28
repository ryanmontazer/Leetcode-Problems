# Time: O(mn)
# Space: O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result+=4
                    if i-1>=0 and grid[i-1][j]:
                        result-=2
                    if j-1>=0 and grid[i][j-1]:
                        result-=2
        return result
