class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        def doCombinations(currSum, currList, currI):
            nonlocal ret
            if currSum == target:
                ret.append(currList)
                return
            for i in range(currI, len(nums)):
                if currSum + nums[i] <= target:
                    currListAppended = currList[:]
                    currListAppended.append(nums[i])
                    doCombinations(currSum + nums[i], currListAppended, i)
        
        doCombinations(0, [], 0)
        return ret