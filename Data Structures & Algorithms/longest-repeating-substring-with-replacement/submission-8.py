class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        charDict = dict()
        maxLen = 0
        while r < len(s):
            if r == 0:
                charDict[s[r]] = charDict.get(s[r], 0) + 1
            # get currK
            maxUnique = 0
            for c in charDict:
                maxUnique = max(maxUnique, charDict[c])
            currK = r - l + 1 - maxUnique
            if currK > k:
                charDict[s[l]] -= 1
                l += 1
            else:
                maxLen = max(maxLen, r - l + 1)
                print(f'r is {r} and l is {l}')
                print(charDict)
                r += 1
                if r < len(s):
                    charDict[s[r]] = charDict.get(s[r], 0) + 1

        return maxLen

            