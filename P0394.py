class Solution:
    def decodeString(self, s: str) -> str:
        integers="0123456789"
        length=len(s)
        if length<2:
            return s
        if s[0] not in integers:
            return s[0]+ self.decodeString(s[1:])
        if s[0] in integers:
            number,curr=s[0],1
            while s[curr] in integers:
                number=number+s[curr]
                curr+=1
        number=int(number)
        curr_begin,curr_end=curr,curr+1
        #determining curr_end
        balance=0
        while True:
            if s[curr]=="[":
                balance+=1
            if s[curr]=="]":
                balance-=1
            if balance==0:
                curr_end=curr
                break
            else:
                curr=curr+1
        result=""
        for i in range(0,number):
            result=result + self.decodeString(s[curr_begin+1:curr_end])
        return result+self.decodeString(s[curr_end+1:])
