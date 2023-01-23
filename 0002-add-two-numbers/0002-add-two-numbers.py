# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum1 = 0
        sum2 = 0
        total = 0
        i = 1
        while l1:
            sum1 = l1.val * i + sum1
            l1 = l1.next
            i *= 10
        i = 1
        while l2:
            sum2 = l2.val* i + sum2
            l2 = l2.next
            i *= 10
        total = sum1 + sum2
        head = ListNode(total % 10)
        curr = head
        total = total // 10
        while total:
            node = ListNode(total % 10)
            curr.next = node
            curr = curr.next
            total = total // 10
        return head
    