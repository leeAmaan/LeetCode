class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt_num = Counter(nums)
        res = 0
        # print(cnt_num.values())
        for value in cnt_num.values():
            # print(value)
            if value == 1:
                return -1 
            else: 
                if value%3==0:
                    res += value//3
                else:
                    res += value//3+1
        return res
        
        
        
#         for i in range(len(nums)):
#             if nums.count(i) == 1:
#                 return False
#         nums = nums.sort()
        
        
#         if nums
#         nums
        
        