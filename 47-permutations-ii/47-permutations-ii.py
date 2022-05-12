class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            result = [p[:i] + [n] + p[i:]
                     for p in result
                     for i in range((p + [n]).index(n) + 1)]
        return result