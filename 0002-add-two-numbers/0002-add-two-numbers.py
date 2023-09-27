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
        i = 1
        while l1:
            sum1 = l1.val * i + sum1
            l1 = l1.next
            i *= 10
        i = 1
        while l2:
            sum2 = l2.val * i + sum2
            l2 = l2.next
            i *= 10
        total_sum = sum1 + sum2
        print(total_sum)
        dummy = ListNode()
        curr = dummy
        if total_sum == 0:
            return ListNode(0)
        while total_sum != 0:
            curr.next = ListNode(total_sum % 10)
            total_sum //= 10
            curr = curr.next
        return dummy.next
        