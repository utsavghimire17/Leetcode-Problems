# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        container = set()
        curr = head
        while curr:
            if curr in container:
                return curr
            container.add(curr)
            curr = curr.next
        