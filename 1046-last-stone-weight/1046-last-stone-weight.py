class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) >= 2:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -1* ((-1*first) - (-1*second)))
        if not stones:
            return 0
        return -1 * heapq.heappop(stones)   