class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        for i in range(n-2, -1, -1):
            ans[i]=nums[i+1]*ans[i+1]
        b=1
        for j in range(1, n):
            b*=nums[j-1]
            ans[j]*=b
        return ans
#         ans = []
#         for i in range(len(nums)-1):
#             mid = nums 
#             del mid[i]
#             a = self.multiply(mid)
#             ans.append(a)
#         return ans 
    
#     def multiply(self, lst):
#         res = 1
#         for n in lst:
#             if n == 0:
#                 return 0
#             res *= n 
#         return res