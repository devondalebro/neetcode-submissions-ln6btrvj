class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreq = {}
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1
            
        cFreq = {}
        nRemaining = len(t)

        l, r = 0, 0

        minLen = len(s) + 1
        minL, minR = 0, 0

        rMoved = True
        while r < len(s):
            print(f"{s[l:r + 1]}")
            cL, cR = s[l], s[r]

            if rMoved and cR in tFreq:
                rMoved = False
                cFreq[cR] = cFreq.get(cR, 0) + 1
                if cFreq[cR] <= tFreq[cR]:
                    nRemaining -= 1

            if nRemaining == 0:
                if r - l + 1 < minLen:
                    minL, minR = l, r
                    minLen = r - l + 1

                l += 1
                if cL in tFreq:
                    cFreq[cL] -= 1
                    if cFreq[cL] < tFreq[cL]:
                        nRemaining += 1
                
                if r - l + 1 < len(t):
                    rMoved = True
                    r += 1
            else:
                rMoved = True
                r += 1

            print(cFreq)

        if minLen != len(s) + 1:
            return s[minL:minR + 1]
        else:
            return ""
            