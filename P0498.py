class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n =len(mat) , len(mat[0])
        result=[]
        for diag in range(1,m+n):
            if diag % 2 ==1 and diag<=m: 
                for i in range(0,diag):
                    if diag-i-1<0 or diag-i-1>m-1 or i>n-1:
                        break
                    result.append(mat[diag-i-1][i])
            if diag % 2 ==1 and diag>m: 
                for i in range(0,m):
                    if diag-m+i>n-1:
                        break
                    result.append(mat[m-1-i][diag-m+i])                    
            if diag % 2 == 0 and diag<=n: 
                for i in range(0,diag):
                    if i>m-1:
                        break
                    result.append(mat[i][diag-i-1])
            if diag % 2 ==0 and diag>n: 
                for i in range(0,diag-n+m):
                    if diag-n+i<0 or diag-n+i>m-1 or n-i-1>n-1 or n-i-1<0:
                        break
                    result.append(mat[diag-n+i][n-i-1])
        return result
