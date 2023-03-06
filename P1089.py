class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length=len(arr)
        i=0
        while i<length:
            if arr[i]==0:
                for j in range(length-1,i+1,-1):
                    arr[j]=arr[j-1]
                if i+1<length:
                    arr[i+1]=0
                i+=2
            else:
                i+=1
