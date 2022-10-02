class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [1] + [0 for _ in range(target)]
        print(dp)
        for _ in range(n):
            for t in range(target, -1, -1):
                dp[t] = sum(dp[max(0, t-k):t])
                print(dp[t], t)
        print(dp)
        return dp[target] % (10**9 + 7)
    
    