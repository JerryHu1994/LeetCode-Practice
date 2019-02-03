# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if len(s)==0:   return None
        i = 0
        while i<len(s) and s[i]!="(" and s[i]!=")":
            i+=1
        root = TreeNode(int(s[:i]))
        # left node
        j, cnt = i+1, 1
        while j<len(s):
            if s[j]=="(":
                cnt += 1
            elif s[j]==")":
                cnt -= 1
            if cnt == 0:
                root.left = self.str2tree(s[i+1:j])
                break
            j+=1
        # right node
        root.right = self.str2tree(s[j+2:-1])
        return root