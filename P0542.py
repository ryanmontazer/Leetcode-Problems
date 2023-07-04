# Time: O(mn)
# Space: O(1)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols,queue= len(mat), len(mat[0]),[]
        direction=[[-1,0],[1,0],[0,-1],[0,+1]]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1:
                    mat[i][j]=float("inf")
                else:
                    queue.append([i,j])
        while queue:
            i,j=queue.pop(0)
            for d1,d2 in direction:
                if i+d1>=0 and i+d1<rows and j+d2>=0 and j+d2<cols and mat[i+d1][j+d2]>mat[i][j]+1:
                    queue.append([i+d1,j+d2])
                    mat[i+d1][j+d2]=mat[i][j]+1
        return mat
