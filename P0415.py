# Time: O(n)
# Space: O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result,carry="",0
        for i in range(max(len(num1),len(num2))):
            if len(num1)-1-i>=0:
                carry+=int(num1[-1-i])
            if len(num2)-1-i>=0:
                carry+=int(num2[-1-i])
            result=str(carry%10)+result
            carry=carry//10
        if carry:
            result=str(carry)+result
        return result
