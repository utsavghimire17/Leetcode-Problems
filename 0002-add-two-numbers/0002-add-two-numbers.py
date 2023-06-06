# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        curr = l1
        i = 1
        while curr:
            sum1 = curr.val * i + sum1
            curr = curr.next
            i *= 10
        i = 1
        curr = l2
        while curr:
            sum2 = curr.val * i + sum2
            curr = curr.next
            i *= 10
        total = sum1 + sum2
        head = ListNode(total % 10)
        total //= 10
        curr = head
        while total:
            node = ListNode(total % 10)
            curr.next = node
            curr = curr.next
            total //= 10
        return head
            