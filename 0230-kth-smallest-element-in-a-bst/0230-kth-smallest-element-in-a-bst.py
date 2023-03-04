# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        stack = []
        curr = root
        while curr:
            stack.append(curr)
            curr= curr.left
            while curr is None and stack:
                node = stack.pop()
                k -= 1
                if k == 0:
                    return node.val
                curr = node.right
        
        