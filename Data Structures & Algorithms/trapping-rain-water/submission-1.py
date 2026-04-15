class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        tot = 0

        left_bound = [0] * len(height)
        maxH = 0
        for i, h in enumerate(height):
            left_bound[i] = maxH
            maxH = max(maxH, h)
        
        right_bound = [0] * len(height)
        maxH = 0
        for i, h in enumerate(reversed(height)):
            right_bound[i] = maxH
            maxH = max(maxH, h)
        
        right_bound.reverse()
        
        area = 0
        for i, h in enumerate(height):
            a = min(left_bound[i], right_bound[i]) - h
            if a > 0:
                area += a

        return area