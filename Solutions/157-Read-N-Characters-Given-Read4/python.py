# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        currbuf = ['']*4
        while count < n:
            # try to read 4
            currcount = read4(currbuf)
            if not currcount:
                return count
            for i in range(currcount):
                buf[count] = currbuf[i]
                count += 1
                if count == n:  return n
        return n