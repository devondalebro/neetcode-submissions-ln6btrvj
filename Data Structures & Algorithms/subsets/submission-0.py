class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def doSubsets(subset, curr):
            if subset is None:
                print('n')
            nonlocal ret
            if curr == len(nums):
                ret.append(subset[:])
            else:
                doSubsets(subset[:], curr + 1)
                subsetWithCurr = subset[:]
                subsetWithCurr.append(nums[curr])
                doSubsets(subsetWithCurr, curr + 1)
        
        doSubsets([], 0)
        return ret
            