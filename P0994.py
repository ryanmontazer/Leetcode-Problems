class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #count is total number of fres oranges in the table
        count,steps=0,0
        for i in range(len(grid)):
            count+=grid[i].count(1)
        grid_temp=deepcopy(grid)
        while True:
            new_element=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and ((i>0 and grid[i-1][j]==2) or (j>0 and grid[i][j-1]==2) or (i+1<len(grid) and grid[i+1][j]==2) or (j+1<len(grid[0]) and grid[i][j+1]==2)):
                        grid_temp[i][j]=2
                        new_element+=1
                        count-=1
            grid=deepcopy(grid_temp)
            if new_element==0 and count!=0:
                return -1
            elif new_element==0 and count==0:
                return steps
            elif new_element>0 and count==0:
                return steps+1
            else:
                steps+=1
