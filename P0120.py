# Time: O(n^2)
# Space: O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        raw=copy.deepcopy(triangle[0])
        temp=[0 for _ in range(len(triangle))]
        for i in range(1,len(triangle)):
            temp[i]=raw[i-1]+triangle[i][i]
            for j in range(i):
                if j==0:
                    temp[j]=raw[0]+triangle[i][0]
                else:
                    temp[j]=triangle[i][j]+min(raw[j-1],raw[j])
            raw=copy.deepcopy(temp[:i+1])
        return min(raw)
