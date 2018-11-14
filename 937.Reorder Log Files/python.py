class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        logfiles = [l.split() for l in logs]
        letterlogs, digitlogs = [], []
        for l in logfiles:
            if l[1].isdigit():
                digitlogs.append(" ".join(l))
            else:
                letterlogs.append((l[1:], l[0], " ".join(l)))
        letterlogs = sorted(letterlogs, key = lambda x:[x[0], x[1]])
        return [l[2] for l in letterlogs] + digitlogs