# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        print pre, post
        if len(pre) == 0 or len(post) == 0: return None
        root = TreeNode(pre[0])
        pre, post = pre[1:], post[:-1]
        if len(pre) == 0 or len(post) == 0: return root
        leftroot, rightroot = pre[0], post[-1]
        if leftroot == rightroot:
            root.left = self.constructFromPrePost(pre, post)
        else:
            root.left = self.constructFromPrePost(pre[:pre.index(post[-1])], post[:post.index(pre[0])+1])
            root.right = self.constructFromPrePost(pre[pre.index(post[-1]):], post[post.index(pre[0])+1:])
        return root