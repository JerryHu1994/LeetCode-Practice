class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        count_T = collections.defaultdict(int)
        for t in T: count_T[t] += 1
        ret = ""
        for s in S:
            if s in T:
                ret += s*count_T[s]
                del count_T[s]
        for k,v in count_T.iteritems():
            ret += k*v
        return ret