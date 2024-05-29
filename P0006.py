# Time: O(n)
# Space: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        array=["" for _ in range(numRows)]
        for i in range(len(s)):
            char=s[i]
            i=i%(2*numRows-2)
            if i<numRows:
                array[i]+=char
            else:
                array[numRows-i-2]+=char
        return "".join(array)
