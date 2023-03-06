class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n,islands= len(grid),len(grid[0]),0
        visited=set()
        for i in range(0,m):
            for j in range(0,n):
                visited.add((i,j))
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        while visited:
            element=visited.pop()
            i,j=element[0],element[1]
            value=grid[i][j]
            extended_element={element}
            element_q=[[i,j]]
            while element_q:
                new_element=element_q.pop(0)
                i1,j1=new_element[0],new_element[1]
                for _ in direction:
                    new_i,new_j=i1+_[0],j1+_[1]
                    if new_i>=0 and new_i<m and new_j>=0 and new_j<n and grid[new_i][new_j]==value and not (new_i,new_j) in extended_element:
                        element_q.append([new_i,new_j])
                        extended_element.add((new_i,new_j))
            visited=visited-extended_element
            if value=='1':
                islands+=1
        return islands
