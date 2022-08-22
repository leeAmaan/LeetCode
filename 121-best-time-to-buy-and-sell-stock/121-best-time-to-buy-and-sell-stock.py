class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        curSum = 0 
        for i in range(n-1):
            curSum += prices[i+1] - prices[i]
            
            if curSum < 0:
                curSum=0
            ans = max(ans, curSum)
        
        return ans
        