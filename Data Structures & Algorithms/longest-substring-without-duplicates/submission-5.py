class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        p1 = 0
        p2 = 1
        longest = 0
        aSet = set()
        while p2 < len(s):
            aSet.add(s[p1])
            while s[p2] in aSet:
                aSet.remove(s[p1])
                p1 += 1
            longest = max(longest, p2 - p1 + 1)
            aSet.add(s[p2])
            p2 += 1
        
        return longest