class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()

        for num in nums:
            num_set.add(num)

        max_len = 0
        for num in nums:
            if num - 1 not in num_set:
                # start of sequence
                curr_len = 1
                while num + curr_len in num_set:
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
                
        return max_len