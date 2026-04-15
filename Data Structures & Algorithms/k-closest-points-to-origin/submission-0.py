import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = p[0] ** 2 + p[1] ** 2
            heapq.heappush(heap, (-dist, p))
        for i in range(len(points) - k):
            heapq.heappop(heap)
        ret = []
        while len(heap) > 0:
            pop = heapq.heappop(heap)
            ret.append(pop[1])
        return ret