# Time: O(n)
# Space: O(1)
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n,result=len(mat),0
        if (n%2)==1:
            result-=mat[n//2][n//2]
        for i in range(n):
            result+=mat[i][n-1-i]
            result+=mat[i][i]
        return result
