class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1list, v2list = [int(i) for i in version1.split(".")], [int(i) for i in version2.split(".")]
        cmplen = min(len(v1list), len(v2list))
        for i in range(cmplen):
            if v1list[i] > v2list[i]:
                return 1
            elif v1list[i] < v2list[i]:
                return -1
        if len(v1list) == len(v2list):  return 0
        longer = 1 if len(v1list) > len(v2list) else -1
        remain = v1list[cmplen:] + v2list[cmplen:]
        return 0 if all([i==0 for i in remain]) else longer
        
        
        