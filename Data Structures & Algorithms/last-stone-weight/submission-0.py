import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -abs(x - y))            
        
        if len(heap) == 1:
            return -heapq.heappop(heap)
        else:
            return 0