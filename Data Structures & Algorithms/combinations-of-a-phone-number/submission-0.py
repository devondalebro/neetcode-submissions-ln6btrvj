class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        ret = []

        if len(digits) == 0:
            return ret

        def dfs(cur, i):
            if i == len(digits):
                nonlocal ret
                ret.append(cur[:])
                return
            
            for c in numMap[digits[i]]:
                cur += c
                dfs(cur, i + 1)
                cur = cur[:-1]
        
        dfs("", 0)
        return ret
