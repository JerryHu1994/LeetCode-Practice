class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.splitlines()
        path, ret = {0:0}, 0
        for line in lines:
            name = line.lstrip("\t")
            currlevel = len(line) - len(name)
            if "." in name:
                # it is a file
                ret = max(ret, path[currlevel] + len(name))
            else:
                # it is a folder
                path[currlevel+1] = path[currlevel] + 1 + len(name)
        return ret