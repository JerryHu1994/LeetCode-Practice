class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        currset = set([0])
        for i in s:
            nextset = set()
            for c in currset:
                if i == "(":
                    nextset.add(c+1)
                elif i == ")":
                    if c-1 >= 0:    nextset.add(c-1)
                else:
                    nextset.add(c+1)
                    if c-1 >= 0:    nextset.add(c-1)
                    nextset.add(c)
            currset = nextset
        print currset
        return 0 in currset