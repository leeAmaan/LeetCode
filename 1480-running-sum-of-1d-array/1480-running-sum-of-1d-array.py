class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sol = 0 
        return [sol:=sol + v for _, v in enumerate(nums)]