# Time: O(m+n)
# Space: O(1)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        raw,col,total=len(grid)-1,0,0
        while raw>-1:
            if grid[raw][col]<0:
                total+=len(grid[0])-col
                raw-=1
            else:
                if col<len(grid[0])-1:
                    col+=1
                else:
                    raw-=1
        return total
