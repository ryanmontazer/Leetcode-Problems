# Time: O(nlog(n))
# Space: O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrival=sorted(zip(position,speed), reverse = True)
        stack=[]
        for pos,speed in arrival:
            arrival_time=(target-pos)/speed
            if not stack or arrival_time>stack[-1]:
                stack.append(arrival_time)
        return len(stack)
