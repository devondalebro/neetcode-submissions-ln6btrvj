class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        floors = len(cost)
        dp = [-1] * (floors + 1)
        def minCost(f):
            if f == 0 or f == 1:
                return 0
            if dp[f] >= 0:
                return dp[f]
            else:
                dp[f] = min(minCost(f - 2) + cost[f - 2], minCost(f - 1) + cost[f - 1])
            return dp[f]
        for f in range(floors + 1):
            minCost(f)
        return dp[floors]
