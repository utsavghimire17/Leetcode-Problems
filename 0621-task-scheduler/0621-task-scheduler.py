class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        heap = []
        count = {}
        time = 0
        for val in tasks:
            count[val] = 1 + count.get(val,0)
        for val in count.values():
            heap.append(-1 * val)
        heapq.heapify(heap)
        while len(heap) or queue:
            time += 1
            if heap:
                max_elem = heapq.heappop(heap)
                max_elem += 1
                if max_elem:
                    queue.append([max_elem, time + n ])
            if queue and queue[0][1] == time:
                queued_task = queue.popleft()
                heapq.heappush(heap,queued_task[0])
            
        return time