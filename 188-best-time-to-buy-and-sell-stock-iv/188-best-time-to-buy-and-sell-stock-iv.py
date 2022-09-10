class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # count, n = k, len(prices)
        
        if not prices:
            return 0 
        
        if k >= len(prices) // 2:
            return sum(
                x-y
                for x,y in zip(prices[1:], prices[:-1])
                if x > y)
        #print(profits(prices[1:]))
        profits = [0]*len(prices)
        print(profits)
        
        for i in range(k):
            preprofit = 0
            
            for j in range(1, len(prices)):
                
                profit = prices[j] - prices[j-1]
                preprofit = max(preprofit+profit, profits[j])
                profits[j] = max(profits[j-1], preprofit)
                
                
        return profits[-1]
                
            
        