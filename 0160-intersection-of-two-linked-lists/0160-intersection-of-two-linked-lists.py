# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp = set()
        count = 0
        currA = headA
        currB = headB
        while currA:
            temp.add(currA)
            currA = currA.next
        while currB:
            if currB in temp:
                return currB
            currB = currB.next
        return 