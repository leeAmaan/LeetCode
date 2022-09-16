class Solution:
    def maximumScore(self, nums: List[int], m: List[int]) -> int:
        k = len(m)
        @lru_cache(None)
        def dfs(i, j, k):
            if k == len(m):
                return 0
            return max(nums[i] * m[k] + dfs(i + 1, j, k + 1), nums[j] * m[k] + dfs(i, j - 1, k + 1))
			
        res = dfs(0, len(nums) - 1, 0) 
        dfs.cache_clear()
        return res
        
        
        
        
        
        #m = len(multipliers)
        #res = 0
        #for i in range(m):
        #    if nums[i] => nums[-(i+1)]:
        #        res += num[i] * multipliers[i]
        #        del nums[i]
        #    elif nums[i] < nums[-(i+1)]:
        #        res += num[-(i+1)] * multipliers[i]
        #        del nums[-(i+1)]
        #    else nums.count == 1: 
        #        res += num[i] * multipliers[i]
        #        del nums[i]
                
        #return  res
                
                