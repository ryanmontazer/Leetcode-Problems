class Solution:
    def removeStars(self, s: str) -> str:
        array=[]
        for i in range(len(s)):
            if not array:
                array.append(s[i])
            elif array[-1]=="*" and s[i]!="*":
                array.pop()
            elif array[-1]=="*" and s[i]=="*":
                array.append("*")
            elif array[-1]!="*" and s[i]=="*":
                array.pop()
            elif array[-1]!="*" and s[i]!="*":
                array.append(s[i])
        return "".join(array)
