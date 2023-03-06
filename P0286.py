class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n,inf= len(rooms),len(rooms[0]),2**31-1
        rooms_q=[]
        vector=[[-1,0],[0,-1],[0,1],[1,0]]
        for i in range(0,m):
            for j in range(0,n):
                if rooms[i][j]==0:
                    rooms_q.append([i,j])
        while  rooms_q:
            check=rooms_q.pop(0)
            i,j=check[0],check[1]
            value=rooms[i][j]
            for _ in vector:
                new_i,new_j=i+_[0],j+_[1]
                if new_i>=0 and new_i<m and new_j>=0 and new_j<n and rooms[new_i][new_j]==inf:
                    rooms_q.append([new_i,new_j])
                    rooms[new_i][new_j]=value+1
