# Time: O(n)
# Space: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[str(i+1) for i in range(n)]
        for i in range(n):
            if not (i+1) % 15:
                result[i]="FizzBuzz"
            elif not (i+1) % 3:
                result[i]="Fizz"
            elif not (i+1) % 5:
                result[i]="Buzz"
        return result
