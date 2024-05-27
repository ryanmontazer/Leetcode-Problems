# Time: O(log(n))
# Space: O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        while num >9:
            result=0
            while num>0:
                result+=num % 10
                num=num//10
            num=result
        return num
