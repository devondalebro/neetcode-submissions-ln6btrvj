class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        p1 = 0
        p2 = 1
        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
                p2 = p1 + 1
            else:
                maxP = max(prices[p2] - prices[p1], maxP)
                p2 += 1
        
        return maxP