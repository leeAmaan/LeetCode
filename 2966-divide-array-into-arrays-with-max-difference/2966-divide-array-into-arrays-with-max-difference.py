class Solution:
    def divideArray(self, nums, k):
        v = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i % 3 == 0:
                if nums[i + 2] - nums[i] <= k:
                    v.append([nums[i], nums[i + 1], nums[i + 2]])
                else:
                    return []
        return v