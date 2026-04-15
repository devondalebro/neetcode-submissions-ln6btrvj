class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_traversed = set()

        for num in nums:
            if num in nums_traversed:
                return True
            nums_traversed.add(num)
        
        return False