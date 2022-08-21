import numpy as np 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        p = 1
        
        for i in range(0, len(nums)):
            res.append(p)
            p = p * nums[i]
            
        p = 1
        
        
        for i in range(len(nums) -1, 0 -1, -1):
            res[i] = res[i] * p
            p = p*nums[i]
            
        return res
        
        
        
        
        
        
        
        # print(np.prod(nums))
        # print(nums[1:])
        
        #for i in range(len(nums)):
        #    print(nums.pop(i))
        #    nums_f"{i}" = nums
        #    del num_f"{i}"[i]
        #    return res.append([np.prod(num_f"{i}")])
            
            
            
        