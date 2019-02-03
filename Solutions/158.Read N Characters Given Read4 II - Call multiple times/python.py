# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def __init__(self):
        self.buffer = [""]*4
        self.writePos = 0
        self.readPos = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        for i in range(n):
            if self.readPos == self.writePos:
                self.writePos = read4(self.buffer)
                self.readPos = 0
                if self.writePos == 0:  return i
            buf[i] = self.buffer[self.readPos]
            self.readPos += 1
        return n