class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a= set(nums)
        a = sum(a)*3 -sum(nums)
        a = a/2
        return int(a)
        