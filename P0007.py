# Time: O(log(n))
# Space: O(log(n))
class Solution:
    def reverse(self, x: int) -> int:
        reverse,abs_x="",abs(x)
        while abs_x:
            reverse+=str(abs_x%10)
            abs_x=abs_x//10
        result,power,index=0,1,1
        maximum=2**31-1 if x>0 else 2**31
        while index<=len(reverse):
            if result<=-power*int(reverse[-index])+maximum:
                result+=power*int(reverse[-index])
            else:
                return 0
            index+=1
            power*=10
        return result if x>0 else -result
