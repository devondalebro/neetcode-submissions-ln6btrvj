class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        BIGNUMBA = 10000000
        dp = [-5] * (amount + 1)
        def opt(a):
            if a == 0:
                return 0
            if dp[a] == -5:
                minC = BIGNUMBA
                for c in coins:
                    if c > a or opt(a - c) == -1:
                        continue
                    minC = min(minC, opt(a - c) + 1)
                if minC == BIGNUMBA:
                    dp[a] = -1
                else:
                    dp[a] = minC
            return dp[a]
        return opt(amount)