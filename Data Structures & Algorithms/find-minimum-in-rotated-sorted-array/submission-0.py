class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # cases
        # the minimum is either on the left or the right of the mid


        # when its on the left

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]

            m = l + (r - l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]
