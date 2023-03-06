class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)
        index=length-1
        while True:
            if digits[index]==9 and index != 0:
                digits[index]=0
                index-=1
            if digits[index]==9 and index==0:
                digits[index]=0
                digits.insert(0,1)
                return digits
            if digits[index] != 9:
                digits[index] +=1 
                return digits
