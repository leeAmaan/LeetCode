class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
            #print(m, i)
        return True
     
    
    
    
    
    
    
    
    """stack = []
        for i in range(len(nums)):
            if nums
            stack.append(nums[i])
        
        return len(nums) <= sum(stack)"""