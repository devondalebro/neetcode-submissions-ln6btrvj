class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)

        # first pass
        i = 0
        while i < len(nums):
            if i == 0:
                ret[i] = 1
            else:
                ret[i] = nums[i - 1] * ret[i - 1]
            
            i += 1
        
        # second pass:
        i = len(nums) - 1
        post = 1
        while i >= 0:
            if i == len(nums) - 1:
                ret[i] *= 1
            else:
                post *= nums[i + 1]
                ret[i] *= post

            i -= 1

        return ret
        