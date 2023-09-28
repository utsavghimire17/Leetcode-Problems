# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for l_list in lists:
            curr = l_list
            while curr:
                res.append(curr.val)
                curr = curr.next
        if not res:
            return None
        res.sort()
        head = ListNode(res[0])
        curr = head
        for i in range(1,len(res)):
            curr.next = ListNode(res[i])
            curr = curr.next
        return head