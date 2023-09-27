# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        current = head
        length = 0
        counter = 0
        while curr:
            length += 1
            curr = curr.next
        if length - n - 1 < 0:
            return current.next
        while counter < length - n - 1:
            current = current.next
            counter += 1
        current.next = current.next.next
        return head