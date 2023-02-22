# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        temp = head
        length = 0
        val = 0
        while temp:
            length += 1
            temp = temp.next
        if length == 1 or length == n:
            return curr.next
        while curr.next:
            if val + 1 == length - n:
                curr.next = curr.next.next
            else:
                curr = curr.next
            val += 1
        return head
        