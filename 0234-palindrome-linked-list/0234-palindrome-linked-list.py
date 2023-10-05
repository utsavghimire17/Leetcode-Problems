# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        new_curr = head
        rev_curr = prev
        
        while new_curr and rev_curr:
            if new_curr.val != rev_curr.val:
                return False
            new_curr = new_curr.next
            rev_curr = rev_curr.next
        return True
        
        