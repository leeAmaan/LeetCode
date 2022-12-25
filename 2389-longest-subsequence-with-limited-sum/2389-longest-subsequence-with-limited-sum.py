class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = list(accumulate(sorted(nums)))
        #print(prefix)
        return [bisect_right(prefix, q) for q in queries]
        
        
        
        
        
        """nums.sort() 
        ans = []
        print(nums)
        if nums == None:
            return [0]
        
        for i in range(len(queries)):
            s=0
            for j in range(len(nums)):
                s += nums[j]
                if s < queries[i]:   
                    print(s, nums[j], j)
                else:      
                    ans.append(j+1)
        return ans 
        
        #return i in queries """