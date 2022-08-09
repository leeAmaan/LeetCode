class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        for i in sorted(arr):
            dp[i] = sum(dp[j] * dp.get(i/j, 0) for j in dp if i % j == 0 ) + 1
            print(dp[i])
        
        
        
        return sum(dp.values()) %(10**9 + 7) 