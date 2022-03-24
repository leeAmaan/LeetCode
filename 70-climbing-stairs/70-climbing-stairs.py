class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        self.dp[1]=1
        self.dp[2]=2
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]