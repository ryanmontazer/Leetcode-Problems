class Solution:
    def romanToInt(self, s: str) -> int:
        result,curr=0,len(s)-1
        while curr>-1:
            char=s[curr]
            if char=='I':
                result+=1
            elif char=='V' and curr>0 and s[curr-1]=="I":
                result+=4
                curr-=1
            elif char=='V':
                result+=5
            elif char=="X" and curr>0 and s[curr-1]=='I':
                result+=9
                curr-=1
            elif char=="X":
                result+=10
            elif char=="L" and curr>0 and s[curr-1]=="X":
                result+=40
                curr-=1
            elif char=="L":
                result+=50
            elif char=="C" and curr>0 and s[curr-1]=="X":
                result+=90
                curr-=1
            elif char=="C":
                result+=100
            elif char=="D" and curr>0 and s[curr-1]=="C":
                result+=400
                curr-=1
            elif char=="D":
                result+=500
            elif char=="M" and curr>0 and s[curr-1]=="C":
                result+=900
                curr-=1
            elif char=="M":
                result+=1000
            curr-=1
        return result
