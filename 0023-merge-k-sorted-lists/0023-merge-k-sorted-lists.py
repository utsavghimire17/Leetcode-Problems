# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for l_list in lists:
            curr = l_list
            while curr:
                heapq.heappush(res,curr.val)
                curr = curr.next
        if not res:
            return None
        head = ListNode(heapq.heappop(res))
        curr = head
        while res:
            curr.next = ListNode(heapq.heappop(res))
            curr = curr.next
        return head