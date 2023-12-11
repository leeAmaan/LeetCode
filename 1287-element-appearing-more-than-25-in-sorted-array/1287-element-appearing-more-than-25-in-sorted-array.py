class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return next(i for i in arr if arr.count(i) / len(arr) > 0.25)
        
#         len_arr = len(arr)-1
#         count = 0
#         # if len(arr)==1:
#         #     return arr[0]
#         for i in range(len_arr):    
#             if arr[i]==arr[i+1]:
#                 count += 1
#                 if (count / len(arr)) > 0.25:
#                     return arr[i]
#             else:
#                 count = 0 