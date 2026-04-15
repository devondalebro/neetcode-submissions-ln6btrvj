class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            if i <= 1:
                ways = 1
            else:
                ways = dp[i - 1] + dp[i - 2]
            dp[i] = ways
        return dp[n]
                
