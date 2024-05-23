# Time: O(mn(m+n))
# Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for k in range(len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j]=0.5
                    for k in range(len(matrix[0])):
                        if matrix[i][k]!=0:
                            matrix[i][k]=0.5
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0.5:
                    matrix[i][j]=0
