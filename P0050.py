# Time: O(log(n))
# Space: O(1)
class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x,n=1/x,-n
        result,power=1,x
        while n:
            if n%2:
                result*=power
            power*=power
            n=n//2
        return result

# Time: O(log(n))
# Space: O(log(n))
class Solution2:
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
