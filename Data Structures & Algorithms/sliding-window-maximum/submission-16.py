import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        queue = [-10000] * len(nums)
        qStart, qEnd = 0, 0
        res = [0] * (len(nums) - k + 1)

        l, r = 0, k - 1
        while r < len(nums):
            if l == 0:
                queue[qEnd] = nums[l]
                i = l + 1
                while i < k:
                    if nums[i] > queue[0]:
                        queue[0] = nums[i]
                        qStart, qEnd = 0, 0
                    else:
                        qEnd += 1
                        queue[qEnd] = nums[i]
                    i += 1
                res[0] = queue[0]
            else:
                if nums[r] > queue[qEnd]:
                    tempEnd = qEnd
                    while tempEnd >= qStart and queue[tempEnd] < nums[r]:
                        queue[tempEnd] = nums[r]
                        tempEnd -= 1
                    qEnd = tempEnd + 1
                else:
                    qEnd += 1
                    queue[qEnd] = nums[r]

                res[l] = queue[qStart]

            if nums[l] == queue[qStart]:
                qStart += 1
            if qEnd < qStart:
                qEnd = qStart
            
            print(queue[qStart:qEnd + 1])

            l += 1
            r += 1
        
        return res
