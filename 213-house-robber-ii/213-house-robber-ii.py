class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_solver(nums):
                dp1, dp2 = 0, 0
                for num in nums:
                    dp1, dp2 = dp2+num, max(dp1, dp2)
                return max(dp1, dp2) 
                
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            return max(rob_solver(nums[1:]), rob_solver(nums[:-1]))
        
            
            
            