# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        res = []
        curr = root
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.left
            while curr == None and stack:
                node = stack.pop()
                res.append(node.val)
                curr = node.right
        return res
  