class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        tempMax = 0
        for i, h in enumerate(height):
            if i != 0:
                maxL[i] = tempMax
            tempMax = max(tempMax, h)
        
        tempMax = 0
        for i, h in enumerate(reversed(height)):
            if i != 0:
                maxR[len(height) - i - 1] = tempMax
            tempMax = max(tempMax, h)
        
        print(maxL)
        print(maxR)
        tot = 0
        for i in range(len(height)):
            if height[i] < min(maxL[i], maxR[i]):
                tot += min(maxL[i], maxR[i]) - height[i]
        return tot

