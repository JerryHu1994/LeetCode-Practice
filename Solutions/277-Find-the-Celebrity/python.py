# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(1,n):
            if knows(ret,i):
                ret = i # we are sure that ret does not know people after ret
        # check if people before ret knows ret
        # check if ret does not know people before ret
        for i in range(0,ret):
            if not knows(i,ret):
                return -1
            if knows(ret, i):
                return -1
        # check if people after ret knows ret
        for i in range(ret+1, n):
            if not knows(i, ret):
                return -1
        return ret
        
        