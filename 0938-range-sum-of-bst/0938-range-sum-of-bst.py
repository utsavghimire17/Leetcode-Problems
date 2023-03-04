# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return None
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val >= low and node.val <= high:
                res += node.val
            if node.left and node.val > low: 
                stack.append(node.left)
            if node.right and node.val < high:
                stack.append(node.right)
                
        return res
    
        
        