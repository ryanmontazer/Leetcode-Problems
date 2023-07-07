# Solution 1: Using Two Pointers
# Time: O(log n)
# Space: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        n1,n2=n,n
        while True:
            n1=self.evaluate_squares(n1)
            n2=self.evaluate_squares(self.evaluate_squares(n2))
            if n1==n2:
                break
        if n1==1:
            return True
        else:
            return False
    def evaluate_squares(self,n)-> int:
        result=0
        for char in str(n):
            result+= int(char)**2
        return result

# Solution 2: Using Hash Table
# Time: O(log n)
# Space: O(log n)
class Solution:
    def isHappy(self, n: int) -> bool:
        my_set=set()
        while  n!=1 and not n in my_set:
            new_number=self.evaluate_squares(n)
            my_set.add(n)
            n=new_number
        return n==1
    def evaluate_squares(self,n)-> int:
        result=0
        while n:
            result+=(n % 10)**2
            n=(n- n % 10)/10
        return result

# Solution 3: Using Hash Table
# Time: O(log n)
# Space: O(log n)
class Solution:
    def isHappy(self, n: int) -> bool:
        my_set=set()
        while  n!=1 and not n in my_set:
            new_number=self.evaluate_squares(n)
            my_set.add(n)
            n=new_number
        return n==1
    def evaluate_squares(self,n)-> int:
        result=0
        for char in str(n):
            result+= int(char)**2
        return result
