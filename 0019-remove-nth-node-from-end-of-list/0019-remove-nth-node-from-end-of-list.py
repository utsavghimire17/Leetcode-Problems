# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        count = 0
        new_count = 0
        while temp:
            count += 1
            temp = temp.next
        print(count)
        curr = head
        if count == 1 or count == n:
            return curr.next
        while curr:
            if new_count == count - n - 1 or count == n:
                curr.next = curr.next.next
            curr = curr.next
            new_count += 1
        return head
            