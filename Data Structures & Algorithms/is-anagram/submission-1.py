class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        c_appearances = dict()

        for c in s:
            c_appearances[c] = c_appearances.get(c, 0) + 1
        
        for c in t:
            if c not in c_appearances:
                return False
            elif c_appearances[c] == 0:
                return False
            else:
                c_appearances[c] -= 1

        return True