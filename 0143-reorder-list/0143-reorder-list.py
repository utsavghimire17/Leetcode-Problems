# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #middle_node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse in_place
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
       
        #merge
        new_curr = head
        
        while new_curr != None:
            temp1 = new_curr.next
            temp2 = prev.next
            new_curr.next = prev
            prev.next = temp1
            new_curr = temp1
            prev = temp2
            
      