import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        q = deque()
        tasks = Counter(tasks)
        for t in tasks:
            heapq.heappush(h, (-tasks[t], 0))
        cycle = 0
        # the queue should track the tasks that we are waiting for
        # (count, cycle)
        # the heap should track the tasks with the highest count
        while len(q) != 0 or len(h) != 0:
            while len(q) != 0 and q[0][1] <= cycle:
                front = q.popleft()
                heapq.heappush(h, front)
            
            if len(h):
                # get task with highest count
                task = heapq.heappop(h)
                taskCount = -task[0] - 1
                print(taskCount)
                if taskCount != 0:
                    q.append((-taskCount, cycle + n + 1))
            cycle += 1
        
        return cycle
