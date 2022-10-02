class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                m = 1
                while m <= min(j, k):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-m]) % (10**9 +7)
                    m += 1
            
        return dp[n][target] % (10**9 + 7)