class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        k=(length-k) % length
        for i in range(0,length):
            if complex(nums[i]).imag==0:
                reserve=nums[i]
            else:
                break
            while complex(nums[i]).imag==0:
                if complex(nums[(i+k) % length]).imag==0:
                    nums[i]=nums[(i+k) % length]+1j
                else:
                    nums[i]=reserve+1j
                i=(i+k) % length
        for i in range(0,length):
            nums[i]=int(nums[i].real)
