class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        m,n,index = len(matrix),len(matrix[0]), [0,0]
        while True:
            for i in range(0,n):
                result.append(matrix[index[0]][index[1]+i])
            for i in range(1,m):
                result.append(matrix[index[0]+i][index[1]+n-1])
            if m != 1:
                for i in range(1,n):
                    result.append(matrix[index[0]+m-1][index[1]+n-1-i])
            if n != 1:
                for i in range(1,m-1):
                    result.append(matrix[index[0]+m-1-i][index[1]])
            if min(m,n)<3:
                return result
            else:
                m,n,index=m-2,n-2,[index[0]+1,index[1]+1]
