# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue, ret = [root], []
        while len(queue):
            curr = queue.pop(0)
            if curr != None:
                ret.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                ret.append("#")
        return " ".join([str(i) for i in ret])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split()
        root = None if vals[0] == "#" else TreeNode(int(vals[0]))
        vals.pop(0)
        if root == None:    return root
        queue, nextq = [root], []
        while len(queue):
            for q in queue:
                next_left = vals.pop(0)
                next_right = vals.pop(0)
                leftnode = None if next_left == "#" else TreeNode(int(next_left))
                rightnode = None if next_right == "#" else TreeNode(int(next_right))
                q.left, q.right = leftnode, rightnode
                if leftnode != None:    nextq.append(leftnode)
                if rightnode != None:    nextq.append(rightnode)
            queue, nextq = nextq, []
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))