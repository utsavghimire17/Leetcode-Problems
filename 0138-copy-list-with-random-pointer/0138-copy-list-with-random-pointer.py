"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        oldToNew = {}
        if not head:
            return None
        while curr:
            new_copy = Node(curr.val)
            oldToNew[curr] = new_copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldToNew[curr]
            if curr.next == None:
                copy.next = None
            else:
                copy.next = oldToNew[curr.next]
            if curr.random == None:
                copy.random = None
            else:
                copy.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]
            
        