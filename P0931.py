# Time: O(n^2)
# Space: O(n)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        raw=copy.copy(matrix[0])
        temp=[0 for _ in range(len(matrix[0]))]
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                min_element=raw[j]
                if 0<j:
                    min_element=min(min_element,raw[j-1])
                if j+1<len(matrix[0]):
                    min_element=min(min_element,raw[j+1])
                temp[j]=min_element+matrix[i][j]
            raw=copy.copy(temp)
        return min(raw)
