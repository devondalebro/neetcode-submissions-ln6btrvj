class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        longest = 0
        for num in nums:
            seqLen = 1
            if num - 1 in numSet:
                continue

            while num + 1 in numSet:
                seqLen += 1
                num += 1
            
            longest = max(longest, seqLen)
        
        return longest

