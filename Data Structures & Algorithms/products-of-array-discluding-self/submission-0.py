class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_everything = 1
        num_zeros = 0
        for num in nums:
            if num == 0:
                num_zeros += 1
                continue
            product_everything *= num
        
        if num_zeros > 1:
            return [0] * len(nums)

        ret = []
        for num in nums:
            if num == 0:
                ret.append(int(product_everything))
            else:
                if num_zeros > 0:
                    ret.append(0)
                else:
                    ret.append(int(product_everything / num))
            
        return ret