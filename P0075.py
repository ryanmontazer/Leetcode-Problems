# Time: O(n)
# Space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        last_seen={0:-1,1:-1,2:-1}
        for i in range(len(nums)):
            if nums[i]==2:
                last_seen[2]=i
                continue
            if nums[i]==1:
                if last_seen[2]==-1:
                    last_seen[1]=i
                    continue
                if last_seen[2]!=-1 and last_seen[1]!=-1:
                    nums[last_seen[1]+1],nums[i]=1,2
                    last_seen[1],last_seen[2]=last_seen[1]+1,i
                    continue
                if last_seen[2]!=-1 and last_seen[1]==-1 and last_seen[0]==-1:
                    nums[0],nums[i]=1,2
                    last_seen[1],last_seen[2]=0,i
                    continue
                if last_seen[2]!=-1 and last_seen[1]==-1 and last_seen[0]!=-1:
                    nums[last_seen[0]+1],nums[i]=1,2
                    last_seen[1],last_seen[2]=last_seen[0]+1,i
                    continue
            if nums[i]==0:
                if last_seen[2]==-1 and last_seen[1]==-1:
                    last_seen[0]=i
                    continue
                if last_seen[2]==-1 and last_seen[1]!=-1:
                    nums[last_seen[0]+1],nums[i]=0,1
                    last_seen[0],last_seen[1]=last_seen[0]+1,i
                    continue
                if last_seen[1]==-1 and last_seen[2]!=-1:
                    nums[last_seen[0]+1],nums[i]=0,2
                    last_seen[0],last_seen[2]=last_seen[0]+1,i
                    continue
                if last_seen[1]!=-1 and last_seen[2]!=-1 and last_seen[0]==-1:
                    nums[0],nums[last_seen[1]+1],nums[i]=0,1,2
                    last_seen[0],last_seen[1],last_seen[2]=0,last_seen[1]+1,i
                    continue
                if last_seen[1]!=-1 and last_seen[2]!=-1 and last_seen[0]!=-1:
                    nums[last_seen[0]+1],nums[last_seen[1]+1],nums[i]=0,1,2
                    last_seen[0],last_seen[1],last_seen[2]=last_seen[0]+1,last_seen[1]+1,i
                    continue
        """
        Do not return anything, modify nums in-place instead.
        """
