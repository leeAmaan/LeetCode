class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [num for tup in zip(nums[: n], nums[n :]) for num in tup]
        