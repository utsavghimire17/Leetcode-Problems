# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        final_curr = dummy
        res = []
        final_res = []
        curr = head
        while curr:
            res.append(curr)
            curr = curr.next
        print(res)
        for node in res:
            if node.val != x and node.val < x:
                final_res.append(node.val)
        for node in res:
            if node.val >= x:
                final_res.append(node.val)
        for i in final_res:
            i = ListNode(i)
            final_curr.next = i
            final_curr = final_curr.next
        return dummy.next
        