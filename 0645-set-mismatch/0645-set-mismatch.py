class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) -sum(set(nums))]
        
        # right = list(range(1,len(nums)+1))        
        # visited=set()
        # mid = [x for x in nums if x in visited or (visited.add(x) or False)]
        # return sorted(list(set(right)-set(nums)) + mid)
