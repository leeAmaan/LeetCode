class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0 
        mid = n //7 
        for i in range(mid):
            res += 28 + (i*7)
        
        mod = n - mid * 7
        mid += 1 
        
        for i in range(mod):
            res += (i + mid)
        return res
        
# class Solution:
#     def totalMoney(self, n: int) -> int:
#         result = 0
#         it = n // 7
#         for i in range(it):
#             result += 28 + (i * 7)
        
#         mod = n - it * 7
        
#         it += 1

#         for i in range(mod):
#             result += (i + it)
            
#         return result
        
        
        
#         mid = n//7
#         if mid == 0:
#             ans = n*(n+1)/2
#             return ans
#         else:
#             for i in range(mid):
                
                
        
#         return ans 