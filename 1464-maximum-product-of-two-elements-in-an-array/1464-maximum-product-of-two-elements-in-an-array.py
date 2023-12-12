class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sort = sorted(nums)
        return (sort[-1]-1)*(sort[-2]-1)
        
        
        # for i in range(len(nums)-1):
        #     if nums[i] == max(nums):
        #         num_1 = nums.pop(i)
        #         for j in range(len(nums)-2):
        #             if nums[j] == max(nums):
        #                 num_2 = nums.pop(j)        
        #                 return (num_1 -1)*(num_2 -1)  