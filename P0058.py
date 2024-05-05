class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr,result=len(s)-1,0
        while s[curr]==" ":
            curr-=1
        while curr>=0 and s[curr]!=" ":
            result+=1
            curr-=1
        return result 
