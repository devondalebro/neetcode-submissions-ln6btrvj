class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = -100
        dp = [[None, None] for _ in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        def opt(i, j):
            nonlocal maximum
            if dp[i][j] is None:
                cand = [opt(i - 1, 0) * nums[i], opt(i - 1, 1) * nums[i], nums[i]]
                dp[i][0] = min(cand)
                dp[i][1] = max(cand)
            maximum = max(maximum, dp[i][1])
            return dp[i][j]
        opt(len(nums) - 1, 0)
        print(dp)
        return maximum