import math

class Solution:
    def mySqrt(self, x: int) -> int:
        l, res = 0, x
        while l <= res:
            mid = l + (res-l)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid 
            elif x < mid*mid:
                res = mid - 1
            else:
                l = mid + 1