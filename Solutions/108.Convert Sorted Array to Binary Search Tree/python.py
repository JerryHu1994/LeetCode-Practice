# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:  return None
        if len(nums) == 1:  return TreeNode(nums[0])
        mid = int(len(nums)//2)
        root = TreeNode(nums[mid])
        left, right = self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:])
        root.left, root.right = left, right
        return root
        