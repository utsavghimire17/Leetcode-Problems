# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        curr = dummy
        for i in range(right):
            curr = curr.next
        new_curr_next = curr.next
        for i in range(left - 1):
            prev = prev.next
        new_curr = prev.next
        new_prev = new_curr_next
        prev.next = curr
        while new_curr != new_curr_next:
            temp = new_curr.next
            new_curr.next = new_prev
            new_prev = new_curr
            new_curr = temp
        return dummy.next