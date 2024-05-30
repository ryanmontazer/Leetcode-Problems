# Time: O(mn)
# Space: O(m)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        raw=[0 for _ in range(len(matrix[0]))]
        temp=[0 for _ in range(len(matrix[0]))]
        result=0
        for i in range(len(matrix[0])):
            raw[i]=int(matrix[0][i])
            result=max(result,raw[i])
        for i in range(1,len(matrix)):
            temp[0]=int(matrix[i][0])
            result=max(result,temp[0])
            for j in range(1,len(matrix[0])):
                temp[j]=int(matrix[i][j])*(1+min(temp[j-1],raw[j-1],raw[j]))
                result=max(result,temp[j])
            raw=copy.copy(temp)
        return result*result
