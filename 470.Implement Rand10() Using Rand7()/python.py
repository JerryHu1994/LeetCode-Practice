# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            x, y = rand7()-1, rand7()-1
            ind = 7*y+x
            if ind < 40:
                return ind%10+1