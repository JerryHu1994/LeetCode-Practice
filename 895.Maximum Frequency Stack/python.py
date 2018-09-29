class FreqStack(object):

    def __init__(self):
        self.freq_dic = collections.defaultdict(list)
        self.int_dic = {}
        self.maxfreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x not in self.int_dic:
            self.int_dic[x] = 1
            self.freq_dic[1].append(x)
            self.maxfreq = max(self.maxfreq, 1)
        else:
            self.int_dic[x] = self.int_dic[x] + 1
            self.freq_dic[self.int_dic[x]].append(x)
            self.maxfreq = max(self.int_dic[x], self.maxfreq)

    def pop(self):
        """
        :rtype: int
        """
        ret = self.freq_dic[self.maxfreq].pop()
        self.int_dic[ret] -= 1
        if len(self.freq_dic[self.maxfreq])==0:
            self.maxfreq -= 1
        return ret


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()