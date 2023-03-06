class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length=len(letters)
        #letters are non-decreasing so letters[i]-target>0 is like FFFTTTTT
        #find first T or if all F , then first F
        left,right=0,length-1
        while left<right:
            mid=(left+right)//2
            if letters[mid]>target:
                right=mid
            else:
                left=mid+1
        if letters[right]>target:
            return letters[right]
        else:
            return letters[0]
