class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        floors = len(cost)
        dp = [-1] * (floors + 1)
        dp[0], dp[1] = 0, 0
        for i in range(2, floors + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[floors]