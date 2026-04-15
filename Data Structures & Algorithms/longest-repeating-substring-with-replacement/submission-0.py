class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        longest = 0
        for c in a:
            p1 = 0
            p2 = 0
            numD = 0
            while p2 < len(s):
                if s[p2] is not c:
                    numD += 1
                while numD > k:
                    if s[p1] is not c:
                        numD -= 1
                    p1 += 1
                longest = max(longest, p2 - p1 + 1)
                p2 += 1
        
        return longest