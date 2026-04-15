class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = {}
        for c in s1:
            s1Freq[c] = s1Freq.get(c, 0) + 1

        l, r = 0, len(s1) - 1
        extras = 0 
        temp = {}
        while r < len(s2):
            if l == 0:
                i = 0
                while i <= r:
                    if s2[i] in s1Freq:
                        temp[s2[i]] = temp.get(s2[i], 0) + 1
                        if temp[s2[i]] > s1Freq[s2[i]]:
                            extras += 1
                    else:
                        extras += 1
                    i += 1
            else:
                if s2[r] in s1Freq:
                    temp[s2[r]] = temp.get(s2[r], 0) + 1
                    if temp[s2[r]] > s1Freq[s2[r]]:
                        extras += 1
                else:
                    extras += 1
                
                if s2[l - 1] in s1Freq:
                    temp[s2[l - 1]] -= 1
                    if temp[s2[l - 1]] >= s1Freq[s2[l - 1]]:
                        extras -= 1
                else:
                    extras -= 1

            if extras == 0:
                return True
            l += 1
            r += 1
        
        return False