class Solution:
    def pivotInteger(self, n: int) -> int: 
        # return isinstance(abs(n*(n+1)/2), int) 
        if int(sqrt(n*(n+1)/2)) == sqrt(n*(n+1)/2): 
            return int(sqrt(n*(n+1)/2))
        else: 
            return -1 