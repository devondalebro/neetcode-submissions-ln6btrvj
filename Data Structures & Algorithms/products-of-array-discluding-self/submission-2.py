class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        i = 0
        while i < len(nums):
            if i == 0:
                res[i] = 1
            else:
                res[i] = res[i - 1] * nums[i - 1]
            i += 1
        
        print(res)
        prev_post = 1
        i = len(nums) - 1
        while i >= 0:
            if i != len(nums) - 1:
                prev_post *= nums[i + 1]
                res[i] *= prev_post
            
            i -= 1 
        
        return res