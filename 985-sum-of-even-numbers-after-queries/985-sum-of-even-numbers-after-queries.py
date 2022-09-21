class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(num for num in nums if num % 2 == 0)
        ans = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 ==0:
                s +=nums[idx]
            ans.append(s)
        return ans
        
        
        
        
        #res = [0 for i in range(len(nums))]  
        #for i in range(len(queries)):
        #    nums[queries[i][1]] += queries[i][0]    
        #    for j in nums:
        #        if j % 2 == 0:
        #            res[i] += j             
        #return res