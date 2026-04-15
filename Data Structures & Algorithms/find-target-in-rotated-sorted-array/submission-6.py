class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        prev = -1
        while l <= r:
            m = l + (r - l) // 2
            if m == prev:
                break

            if nums[m] == target:
                return m

            if nums[m] <= nums[r]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            prev = m
        
        return -1
