# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q or not q and p:
            return False
        if not p and not q:
            return True
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            nodep = stack_p.pop()
            nodeq = stack_q.pop()
            if nodep.val != nodeq.val:
                return False
            if nodep.right and not nodeq.right or nodeq.right and not nodep.right:
                return False
            if nodeq.left and not nodep.left or nodeq.left and not nodep.left:
                return False
            if nodep.left and nodeq.left:
                stack_p.append(nodep.left)
                stack_q.append(nodeq.left)
            if nodep.right and nodeq.right:
                stack_p.append(nodep.right)
                stack_q.append(nodeq.right)
        return stack_p == stack_q
        
        
        