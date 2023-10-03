# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        curr = root
        potential = None
        while curr:
            if p.val >= curr.val:
                curr = curr.right
            else:
                potential = curr
                curr = curr.left
        return potential