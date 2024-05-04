# Time: O(n)
# Space: O(n)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a1,b1,c1=bin(a)[2:],bin(b)[2:],bin(c)[2:]
        n,result=max(len(a1),len(b1),len(c1)),0
        a1="0"*(n-len(a1))+a1
        b1="0"*(n-len(b1))+b1
        c1="0"*(n-len(c1))+c1
        for i in range(n):
            if a1[i]+b1[i]+c1[i] in ["100","010","001"]:
                result+=1
            elif a1[i]+b1[i]+c1[i]=="110":
                result+=2
        return result
