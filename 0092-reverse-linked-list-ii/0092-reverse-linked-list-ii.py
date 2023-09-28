# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        for i in range(right): 
            curr = curr.next
        
        temp = curr.next
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        
        new_curr = prev.next
        new_prev = temp
        while new_curr != temp:
            new_temp = new_curr.next
            new_curr.next = new_prev
            new_prev = new_curr
            new_curr = new_temp
        prev.next = new_prev
        return dummy.next