class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        []
        candidates.sort()
        res = []
        def backtrack(currExp, currSum, cur):
            nonlocal res
            if cur == len(candidates):
                if currSum == target:
                    res.append(currExp[:])
                return
            
            if currSum < target:
                newExp = currExp[:]
                newExp.append(candidates[cur])
                backtrack(newExp, currSum + candidates[cur], cur + 1)

            while cur + 1 < len(candidates) and candidates[cur + 1] == candidates[cur]:
                cur += 1
            backtrack(currExp, currSum, cur + 1)
        
        backtrack([], 0, 0)
        return res
