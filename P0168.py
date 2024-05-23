# Time: O(logn)
# Space: O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        my_dict = {i: chr(i + 64) for i in range(1, 27)}
        result=""
        while columnNumber>0:
            columnNumber-=1
            quotient,remainder=columnNumber//26,columnNumber % 26
            result=my_dict[remainder+1]+result
            columnNumber=quotient
        return result
