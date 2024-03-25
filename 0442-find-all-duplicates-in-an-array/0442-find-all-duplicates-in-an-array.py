class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            num = abs(nums[i])
            idx = num -1
            if nums[idx] < 0:
                ans.append(num)
            nums[idx] *= -1
            # print(nums)
        return ans
            
            
#             if nums.count(nums[i]) != 1:
#                 ans.append(nums[i])
        
#         # print(dict(ans))
#         return list(set(ans))