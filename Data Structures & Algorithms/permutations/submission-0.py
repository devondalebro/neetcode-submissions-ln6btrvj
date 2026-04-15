class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def doPermute(p, used):
            nonlocal ret
            if len(p) == len(nums):
                ret.append(p)
            else:
                for n in nums:
                    if n not in used:
                        pNew = p[:]
                        pNew.append(n)
                        usedNew = used.copy()
                        usedNew.add(n)
                        doPermute(pNew, usedNew)
        
        doPermute([], set())
        return ret