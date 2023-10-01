# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        return self.traverse(root,self.res)
    def traverse(self, root, res):
        if root != None:
            self.traverse(root.left, res)
            res.append(root.val)
            self.traverse(root.right,res)
        return res
    
        # stack = []
        # res = []
        # curr = root
        # while curr:
        #     stack.append(curr)
        #     curr = curr.left
        #     while curr == None and stack:
        #         node = stack.pop()
        #         res.append(node.val)
        #         curr = node.right
        # return res
    
        
    
  