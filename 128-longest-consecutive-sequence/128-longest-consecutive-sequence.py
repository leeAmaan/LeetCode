class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, left = 0, set(nums)
        while left:
            l = r = left.pop()
            while l - 1 in left: left.remove(l - 1); l -= 1;
            while r + 1 in left: left.remove(r + 1); r += 1;
            res = max(res, r - l + 1)
        return res
            