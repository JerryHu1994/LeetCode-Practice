class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.queue = []
        ind = 0
        while ind < len(compressedString):
            nextc = compressedString[ind]
            ind += 1
            start = ind
            while ind < len(compressedString) and compressedString[ind].isdigit():
                ind += 1
            count = int(compressedString[start:ind])
            self.queue.append(nextc)
            self.queue.append(count)

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        currchar = self.queue[0]
        self.queue[1] -= 1
        if self.queue[1] == 0:
            self.queue.pop(0)
            self.queue.pop(0)
        return currchar

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()