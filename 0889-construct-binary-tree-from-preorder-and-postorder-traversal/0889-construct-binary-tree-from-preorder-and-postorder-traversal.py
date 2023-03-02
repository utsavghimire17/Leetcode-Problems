# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    index = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        if len(preorder) == 1:
            return TreeNode(postorder.pop())
        root = TreeNode(postorder.pop())
        mid = preorder.index(postorder[-1])
        root.right = self.constructFromPrePost(preorder[mid:],postorder)
        root.left = self.constructFromPrePost(preorder[1:mid],postorder)
        return root