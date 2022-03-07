class Solution:
    def sortColors(self, nums):
        fir, mid, end = 0, 0, len(nums) - 1
        
        while mid <= end:
            if nums[mid] == 0:
                nums[fir], nums[mid] = nums[mid], nums[fir]
                mid += 1
                fir += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            ## 아래는 nums[mid] == 1: 을 의미 
            else:  
                mid += 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        