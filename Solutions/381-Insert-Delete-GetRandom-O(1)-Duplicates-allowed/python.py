class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)
        self.li = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = val in self.dic
        self.dic[val].append(len(self.li))
        self.li.append([val, len(self.dic[val])-1])
        return ret

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if len(self.dic[val]) == 0:
            return False
        if self.dic[val][-1] == len(self.li)-1:
            self.dic[val].pop()
            self.li.pop()
            return True
        # swap with the last entry in the self.li
        lastval, lastidx_indic = self.li[-1]
        removeval, removeidx_inli = val, self.dic[val][-1]
        self.dic[lastval][lastidx_indic] = removeidx_inli
        self.li[removeidx_inli] = [lastval, lastidx_indic]
        self.dic[removeval].pop()
        self.li.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.li[random.randint(0, len(self.li)-1)][0]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()