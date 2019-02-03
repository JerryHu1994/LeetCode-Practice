"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root == None:    return None
        queue, encode = [root], ""
        encode += str(root.val)+"#"
        while len(queue):
            curr = queue.pop(0)
            children = curr.children
            s = " ".join([str(c.val) for c in children])
            queue.extend(children)
            encode += s + "#"
        return encode

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == None:    return None
        sep_list = data.split("#")
        root = Node(int(sep_list[0]), [])
        queue = [root]
        sep_list = sep_list[:-1]
        for child in sep_list[1:]:
            currroot = queue.pop(0)
            splitlist = child.split()
            if len(splitlist) == 0: continue
            child_vals = [int(i) for i in splitlist]
            child_nodes = []
            for i in child_vals:
                newnode = Node(i, [])
                child_nodes.append(newnode)
            currroot.children = child_nodes
            queue.extend(child_nodes)
        return root
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))