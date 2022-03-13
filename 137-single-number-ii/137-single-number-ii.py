class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1<<i) == (1<<i): count += 1
            result |= (count%3) << i
            
        return result if result < (1<<31) else result - (1<<32)
        