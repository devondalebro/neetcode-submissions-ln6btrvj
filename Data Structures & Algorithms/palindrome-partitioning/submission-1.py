class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        def backtrack(cur, i):
            print(cur)
            print(i)
            if i == len(s):
                nonlocal res
                res.append(cur[:])
                return
            
            for j in range(i, len(s)):
                substr = s[i : j + 1]
                if isPalindrome(substr) is not True:
                    continue
                cur.append(substr)
                backtrack(cur, j + 1)
                cur.pop()
        
        backtrack([], 0)
        return res