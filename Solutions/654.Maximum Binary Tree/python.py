# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:  return None
        if len(nums) == 1:  return TreeNode(nums[0])
        idx = nums.index(max(nums))
        root = TreeNode(nums[idx])
        root.left = self.constructMaximumBinaryTree(nums[0:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root
        