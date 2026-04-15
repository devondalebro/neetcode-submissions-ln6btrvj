class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = dict()

        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
        
        sort = [[] for _ in range(len(nums) + 1)]
        for num in occurences:
            print(num)
            sort[occurences[num]].append(num)

        print(sort)
        res = []
        for el in reversed(sort):
            if k == 0:
                break

            if len(el) > 0:
                for e in el:
                    k -= 1
                    res.append(e)
        
        return res
