# Time: O(n)
# Space: O(n)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        array,i=[],0
        while i< len(asteroids):
            if not array or array[-1]<0 or array[-1]*asteroids[i]>0:
                array.append(asteroids[i])
                i+=1
            else:
                if  abs(array[-1])==abs(asteroids[i]):
                    array.pop()
                    i+=1
                elif abs(array[-1])<abs(asteroids[i]):
                    array.pop()
                else:
                    i+=1
        return array
