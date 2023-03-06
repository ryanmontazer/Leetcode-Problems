class Solution:
    def reverseWords(self, s: str) -> str:
        length=len(s)
        s_reverse, s_return="",""
        for i in range(0,length):
            s_reverse =s_reverse + s[length-i-1]
        curr,start=0,-1
        while curr<length: 
            #setting up start the first non space letter if available
            while start == -1 and curr<length:
                if not s_reverse[curr].isspace():
                    start=curr
                else:
                    curr=curr+1
            if start==-1:
                return s_return
            elif len(s_return) != 0 :
                s_return= s_return+" "
            #setting up end
            while True:
                if curr+1 == length:
                    end = curr
                    break
                if curr+1 < length and not s_reverse[curr+1].isspace() :
                    curr = curr+1                    
                if curr+1 < length and s_reverse[curr+1].isspace() :
                    end = curr
                    break
            #reverse and adding the current word from start to end to s beginning from s_curr 
            for j in range(end,start-1,-1):
                s_return=s_return+s_reverse[j]
            #resetting start and end to go to the next word
            curr,start=curr+1,-1
        return s_return
