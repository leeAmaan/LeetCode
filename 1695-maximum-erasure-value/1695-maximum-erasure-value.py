class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        beg, end, s, n, sm = 0, 0, set(), len(nums), 0 
        ans = 0 
        while end < n:
            if nums[end] not in s:
                sm += nums[end]
                s.add(nums[end])
                end += 1
                ans = max(ans, sm)
            else:
                sm -= nums[beg]
                s.remove(nums[beg])
                beg += 1
            
        return ans