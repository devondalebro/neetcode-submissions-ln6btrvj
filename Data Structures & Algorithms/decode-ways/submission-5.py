class Solution:
        
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)
        invalid = False
        def valid(s):
            return int(s) <= 26 and s[0] != "0"
        def opt(i):
            if i == 0:
                return int(valid(s[i]))
            if i == 1:
                return int(valid(s[0]) and valid(s[1])) + int(valid(s[0:2]))
            if dp[i] == -1:
                dp[i] = 0
                if valid(s[i:i+1]):
                    dp[i] += opt(i - 1)
                if valid(s[i-1:i+1]):
                    dp[i] += opt(i - 2)
                if dp[i] == 0:
                    invalid = True
            return dp[i]
        return opt(len(s) - 1) if not invalid else 0