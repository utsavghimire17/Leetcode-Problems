class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        queue = deque()
        heap = []
        count = {}
        time = 0
        for val in tasks:
            count[val] = 1 + count.get(val,0)
        for val in count.values():
            heap.append(val)
        
        while len(heap) or queue:
            heap.sort()
            time += 1
            if heap:
                max_elem = heap.pop()
                max_elem -= 1
                if max_elem > 0:
                    queue.append([max_elem, time + n ])
            if queue and queue[0][1] == time:
                queued_task = queue.popleft()
                heap.append(queued_task[0])
            
        return time