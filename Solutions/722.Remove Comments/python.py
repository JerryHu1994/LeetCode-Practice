class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        inblock, ret = False, []
        for line in source:
            i = 0
            if not inblock: newline = []
            while i < len(line):
                if line[i:i+2] == '/*' and not inblock:
                    inblock = True
                    i += 1
                elif line[i:i+2] == '*/' and inblock:
                    inblock = False
                    i += 1
                elif not inblock and line[i:i+2] == '//':
                    break
                elif not inblock:
                    newline.append(line[i])
                i += 1
            if newline and not inblock:
                ret.append("".join(newline))
        return ret
                    