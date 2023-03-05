# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and not q or q and not p:
            return False
        if not p and not q:
            return True
        stackp = [p]
        stackq = [q]
        while stackp and stackq:
            nodep = stackp.pop()
            nodeq = stackq.pop()
            if nodep.val != nodeq.val:
                return False
            if not nodep.right and nodeq.right or not nodeq.right and nodep.right:
                return False
            if not nodep.left and nodeq.left or not nodeq.left and nodep.left:
                return False
            if nodep.right and nodeq.right:
                stackp.append(nodep.right)
                stackq.append(nodeq.right)
            if nodep.left and nodeq.left:
                stackp.append(nodep.left)
                stackq.append(nodeq.left)
        return True