class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        try:
            inc = [float('inf')] * 2
            for x in nums:
                inc[bisect.bisect_left(inc, x)] = x
            return False
        except:
            return True