# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        array = []
        res = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
        start = 0
        end = len(array) - 1
        while start < end:
            res.append(array[start])
            res.append(array[end])
            start += 1
            end -= 1
        if start == end:
            res.append(array[start])
        print(res)
        if res:
            new_head = ListNode(res[0])
            curr = head
        for i in range(1,len(res)):
            new_node = ListNode(res[i])
            print(new_node.val)
            curr.next = new_node
            curr = curr.next
        return new_head