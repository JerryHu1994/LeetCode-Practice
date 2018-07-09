class TrieNode(object):
    def __init__(self):
        self.map = {}
        self.val = 0

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        curr = self.root
        curr.val += delta
        for i in key:
            curr = curr.map.setdefault(i, TrieNode())
            curr.val += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root
        for i in prefix:
            if i not in curr.map:
                return 0
            curr = curr.map[i]
        return curr.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)