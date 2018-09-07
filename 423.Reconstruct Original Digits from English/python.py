class Solution(object):
    def helper(self, counter, char, num, num_int):
        count = counter[char]
        if count == 0:  return
        for i in num:
            counter[i] -= count
        self.ret += [num_int]*count
    
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        self.ret = []
        self.helper(counter, "z", "zero", 0)
        self.helper(counter, "x", "six", 6)
        self.helper(counter, "w", "two", 2)
        self.helper(counter, "g", "eight", 8)
        self.helper(counter, "t", "three", 3)
        self.helper(counter, "r", "four", 4)
        self.helper(counter, "f", "five", 5)
        self.helper(counter, "i", "nine", 9)
        self.helper(counter, "o", "one", 1)
        self.helper(counter, "s", "seven", 7)
        return "".join(sorted([str(i) for i in self.ret]))