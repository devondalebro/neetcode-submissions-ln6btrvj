class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has_num = set()
        sequences = dict()

        for num in nums:
            has_num.add(num)
        
        for num in nums:
            # check if start of sequence
            if num - 1 not in has_num:
                sequences[num] = 1
                next_num = num + 1
                
                while next_num in has_num:
                    sequences[num] += 1
                    next_num += 1

        max_len = 0
        for sequence in sequences:
            max_len = max(max_len, sequences[sequence])
        
        return max_len
