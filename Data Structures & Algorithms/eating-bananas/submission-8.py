class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search for optimal k
        def can_eat(k):
            hours = 0
            for p in piles:
                hours += (p - 1) // k + 1
            return hours <= h
        
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2
            if can_eat(m):
                r = m
            else:
                l = m + 1
            print(f"left {l} right {r}")
            
        return l

