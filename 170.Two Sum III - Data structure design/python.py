class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if not number in self.li:
            self.li[number] = 1
        else:
            self.li[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.li:
            if value - i in self.li and ((value-i) != i or self.li[value-i] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)