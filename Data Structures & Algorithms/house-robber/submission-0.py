class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums) + 1)
        def robAux(houses): 
            if houses == 0:
                dp[houses] = 0
            elif dp[houses] >= 0:
                return dp[houses]
            else:
                if houses == 1:
                    dp[houses] = nums[houses - 1]
                else:
                    dp[houses] = max(robAux(houses - 1), robAux(houses - 2) + nums[houses - 1])
            return dp[houses]
        return robAux(len(nums))