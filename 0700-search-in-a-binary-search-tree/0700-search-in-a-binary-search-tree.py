# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # curr = root
        # while (curr):
        #     if val == curr.val:
        #         return curr
        #     if val > curr.val:
        #         curr = curr.right
        #     if val < curr.val:
        #         curr = curr.left
        # return None
        
        if root == None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left,val)
        elif root.val < val:
            return self.searchBST(root.right,val)
            