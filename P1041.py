# Time: O(n)
# Space: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr,direction=[0,0],1
        for ins in instructions:
            if ins=="L":
                direction=(direction+1) % 4
            elif ins=="R":
                direction=(direction-1) % 4
            elif ins=="G":
                if direction==1:
                    curr[1]+=1
                elif direction==2:
                    curr[0]-=1
                elif direction==3:
                    curr[1]-=1
                elif direction==0:
                    curr[0]+=1
        if curr==[0,0] or direction!=1:
            return True
        return False
