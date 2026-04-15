class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupSet = set();
        for num in nums:
            if num in dupSet:
                return True
            dupSet.add(num)

        return False