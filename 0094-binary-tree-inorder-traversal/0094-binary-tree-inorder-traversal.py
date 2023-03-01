# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     self.helper(root,res)
    #     return res
    # def helper(self,root,res):
    #     if root != None:
    #         self.helper(root.left,res)
    #         res.append(root.val)
    #         self.helper(root.right,res)
    #     return res
    
        stack = []
        res = []
        curr = root
        while curr:
            stack.append(curr)
            curr = curr.left
            while curr == None and stack:
                node = stack.pop()
                res.append(node.val)
                curr = node.right
        return res
    
        
    
  