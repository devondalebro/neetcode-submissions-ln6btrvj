class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            numSet.add(n)

        longest = 0
        for n in numSet:
            if n - 1 not in numSet:
                currLen = 0
                while n in numSet:
                    n += 1
                    currLen += 1
                longest = max(longest, currLen)
        return longest