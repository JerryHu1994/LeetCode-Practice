# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        num = target
        dirs = []
        while num != 0:
            if num%2 == 1:
                num = (num - 1)//2
                dirs.append("left")
            else:
                num = (num - 2)//2
                dirs.append("right")
        dirs = dirs[::-1]
        curr = self.root
        for di in dirs:
            if curr == None:    return False
            if di == "left":
                curr = curr.left
            else:
                curr = curr.right
        return curr != None


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)