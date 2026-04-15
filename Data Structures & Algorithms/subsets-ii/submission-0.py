class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        def doSubsets(cur, i):
            nonlocal ret
            if i == len(nums):
                ret.append(cur[:])
                return
            
            newCur = cur.copy()
            newCur.append(nums[i])
            doSubsets(newCur, i + 1)
            newCur.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            doSubsets(newCur, i + 1)
        
        doSubsets([], 0)
        return ret
                