import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)

        for i in range(len(nums) - k):
            heapq.heappop(heap)
        return heap[0]