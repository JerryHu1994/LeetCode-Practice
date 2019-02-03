# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if len(s) == 0: return None
        if s[0] != "[":
            return NestedInteger(int(s))
        s = s[1:-1]
        ind = 0
        res = NestedInteger()
        while ind < len(s):
            if s[ind].isdigit() or s[ind] == "-":
                sign = -1 if s[ind] == "-" else 1
                if s[ind] == "-":
                    ind += 1
                start = ind
                while ind < len(s) and s[ind].isdigit():
                    ind += 1
                res.add(NestedInteger(sign*int(s[start:ind])))
            elif s[ind] == ",":
                ind += 1
            else:
                start = ind
                cnt = 1
                ind += 1
                while cnt != 0:
                    if s[ind] == "[":
                        cnt += 1
                    elif s[ind] == "]":
                        cnt -= 1
                    ind += 1
                res.add(self.deserialize(s[start:ind]))
        return res