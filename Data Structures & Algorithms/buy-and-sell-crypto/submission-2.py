class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minSoFar = prices[0]
        for p in prices:
            minSoFar = min(minSoFar, p)
            maxP = max(maxP, p - minSoFar)
        return maxP