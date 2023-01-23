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
        total_str = str(total)
        print(total_str)
        head = ListNode(int(total_str[-1]))
        curr = head
        for i in range(len(total_str)-2,-1,-1):
            node = ListNode(int(total_str[i]))
            curr.next = node
            curr = curr.next
        return head
    