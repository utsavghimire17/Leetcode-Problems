# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        """
        stack = []
        if root is None:
            return None
        curr = root
        pre = None
        while curr:
            stack.append(curr)
            curr = curr.left
            while curr is None and stack:   
                node = stack.pop()
                if pre is not None and pre.val >= node.val:
                    return False
                pre  = node
                curr = node.right
               
        return True