# Time: O(n)
# Space: O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cordinate=[0,0]
        for char in moves:
            if char=="R":
                cordinate[0]+=1
            elif char=="L":
                cordinate[0]-=1
            elif char=="U":
                cordinate[1]+=1
            elif char=="D":
                cordinate[1]-=1
        return cordinate==[0,0] 
