# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser_dummy = ListNode()
        l_curr = lesser_dummy
        greater_dummy = ListNode()
        h_curr = greater_dummy
        curr = head
        while curr:
            if curr.val < x:
                l_curr.next = curr
                l_curr = l_curr.next
            elif curr.val >= x:
                print(curr.val)
                h_curr.next = curr
                h_curr = h_curr.next
            curr = curr.next
        h_curr.next = None
        l_curr.next = greater_dummy.next
        return lesser_dummy.next