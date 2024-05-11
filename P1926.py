# Time: O(mn)
# Space: O(mn)
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue,visited=[[entrance[0],entrance[1],0]],{(entrance[0],entrance[1])}
        while queue:
            element=queue.pop(0)
            i,j,k=element[0],element[1],element[2]+1
            for [nx,ny] in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny]=="." and (nx,ny) not in visited:
                    if nx in [0,len(maze)-1] or ny in [0,len(maze[0])-1]:
                        return k
                    queue.append([nx,ny,k])
                    visited.add((nx,ny))
        return -1
