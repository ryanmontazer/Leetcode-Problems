# Time: O(n)
# Space: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[1]*len(temperatures)
        stack=[0]
        for i in range(1,len(temperatures)):
            if stack and temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack :
                    index=stack[-1]
                    if temperatures[index]<temperatures[i]:
                        result[index]=i-index
                        stack.pop()
                    else:
                        break
                stack.append(i)
        while stack:
            result[stack.pop()]=0
        return result
