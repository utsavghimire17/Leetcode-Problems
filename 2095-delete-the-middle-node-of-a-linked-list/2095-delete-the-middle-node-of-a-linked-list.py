# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        curr = head
        middle_node = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow == fast:
            return None
        middle_node = slow
        while curr.next and curr.next != middle_node:
            curr = curr.next
        curr.next = curr.next.next
        return head
        