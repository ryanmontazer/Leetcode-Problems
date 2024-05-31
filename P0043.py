# Time: O(mn)
# Space: O(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def summation(s1: str, s2: str) -> str:
            result,carry,i="",0,0
            while i<max(len(s1),len(s2)) or carry:
                if i<len(s1):
                    carry+=int(s1[-i-1])
                if i<len(s2):
                    carry+=int(s2[-i-1])
                result=str(carry%10)+result
                carry=carry//10
                i+=1
            return result
        def multiplication(s1:str, char:str) -> str:
            result,carry,i="",0,0
            while i<len(s1) or carry:
                if i<len(s1):
                    carry+=int(s1[-i-1])*int(char)
                result=str(carry%10)+result
                carry=carry//10
                i+=1
            return result
        if num1=="0" or num2=="0":
            return "0"
        result="0"
        for i in range(len(num2)):
            result=summation(result,multiplication(num1,num2[-i-1])+"0"*i)
        return result
