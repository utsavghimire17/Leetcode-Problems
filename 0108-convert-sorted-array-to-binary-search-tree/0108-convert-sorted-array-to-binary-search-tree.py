# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
            
        def insert_node(l,r):
            if l > r:
                return
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = insert_node(l, mid - 1)
            root.right = insert_node(mid + 1, r)
            
            return root
        return insert_node(0, len(nums) - 1)
        