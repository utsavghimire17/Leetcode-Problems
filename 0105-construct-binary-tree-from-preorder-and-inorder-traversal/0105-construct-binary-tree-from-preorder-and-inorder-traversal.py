# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        self.index = 0
        for i,v in enumerate(inorder):
            index_map[v]  = i
        def recur(low, high):
            if low > high:
                return None
            root = TreeNode(preorder[self.index])
            mid_index = index_map[root.val]
            self.index += 1
            root.left = recur(low, mid_index-1)
            root.right = recur(mid_index+1, high)
            return root
        return recur(0, len(inorder)-1)
            