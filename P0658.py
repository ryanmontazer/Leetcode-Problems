class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        xdistance=[]
        length=len(arr)        
        left,right=0,length-1
        count=-1
        #count is the last place arr[count] <= x and 0<=count (T T F F F)
        while left<right:
            mid=(left+right+1)//2
            if arr[mid]>x:
                right=mid-1
            else:
                left=mid
        if arr[right]<=x:
            count=right
        #if x<arr[0]: count=-1
        #if x>=arr[length-1]: count=length-1
        cursor_right=count+1  # x < arr[cursor_right]
        cursor_left=count # x >= arr[cursor_left]
        while len(xdistance)<k:
            if cursor_left==-1:
                xdistance.append(arr[cursor_right])
                cursor_right+=1
            elif cursor_right==length:
                xdistance.append(arr[cursor_left])
                cursor_left-=1
            elif (x-arr[cursor_left])<=(arr[cursor_right]-x):
                xdistance.append(arr[cursor_left])
                cursor_left-=1
            else:
                xdistance.append(arr[cursor_right])
                cursor_right+=1
        xdistance.sort()
        return xdistance
