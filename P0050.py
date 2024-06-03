# Time: O(log(n))
# Space: O(log(n))
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x,n=1/x,-n
        stack,result=[],1
        while n:
            if n%2:
                stack.append("plus")
                n-=1
            else:
                stack.append("power")
                n=n//2
        while stack:
            char=stack.pop()
            if char=="plus":
                result*=x
            else:
                result=result*result
        return result
