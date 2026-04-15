class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = 1
        currSet = set()
        alphaSet = set()
        alphaSet.add(s[0])
        l, r = 0, 1
        while r < len(s):
            if s[r] in alphaSet:
                alphaSet.remove(s[l])
                l += 1
            else:
                maxLen = max(maxLen, r - l + 1)
                alphaSet.add(s[r])
                r += 1
        return maxLen
