class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.div = 1000
        self.dic = [[] for i in range(1000)]
        

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashval = key%self.div
        if key not in self.dic[hashval]:
            self.dic[hashval].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashval = key%self.div
        if key in self.dic[hashval]:
            self.dic[hashval].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hashval = key%self.div
        return key in self.dic[hashval]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)