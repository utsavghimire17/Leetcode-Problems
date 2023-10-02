# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                heapq.heappush(heap, -1 * node.val)
                if len(heap) > k:
                    heapq.heappop(heap)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        while len(heap) > k:
            heapq.heappop(heap)
        min_elem = heapq.heappop(heap)
        return -1 * min_elem