class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        temp=[1,1]
        result=[[1],[1,1]]
        for i in range(3,numRows+1):
            #length of temp is i-1
            new_temp=[1]
            for j in range(0,i-2):
                new_temp.append(temp[j]+temp[j+1])
            new_temp.append(1)
            temp=new_temp
            result.append(temp)
        return result
