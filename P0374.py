# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n==1:
            return 1
        index=[1,n]
        while True:
            if guess(index[0])==0:
                return index[0]
            elif guess(index[1])==0:
                return index[1]
            else:
                mid=int((index[0]+index[1])/2)
                if guess(mid)==0:
                    return mid
                elif guess(mid)==-1:
                    index[1]=mid
                else:
                    index[0]=mid
