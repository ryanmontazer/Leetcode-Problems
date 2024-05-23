# Time: O(n)
# Space: O(n)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array=[]
        for char in operations:
            if char=="+":
                array.append(array[-1]+array[-2])
            elif char=="D":
                array.append(2*array[-1])
            elif char=="C":
                array.pop()
            else:
                array.append(int(char))
        return sum(array)
