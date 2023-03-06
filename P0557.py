class Solution:
    def reverseWords(self, s: str) -> str:
        length=len(s)
        s_return=""
        curr,start=0,0
        while True:
            while True:
                if curr+1==length or s[curr+1] == " ":
                    break
                else:
                    curr=curr+1
            for i in range(curr,start-1,-1):
                s_return=s_return+s[i]
            if curr+1==length:
                return s_return
            else:
                curr=curr+2
                start=curr
                s_return=s_return+" "
