# Time: O(log n)
# Space: O(log n)
class Solution:
    def isHappy(self, n: int) -> bool:
        my_dict={}
        while  n!=1 and not n in my_dict:
            new_number=self.evaluate_squares(n)
            my_dict[n]=new_number
            n=new_number
        return n==1
    def evaluate_squares(self,n)-> int:
        result=0
        while n:
            result+=(n % 10)**2
            n=(n- n % 10)/10
        return result
