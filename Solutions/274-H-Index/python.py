class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        cnt = collections.Counter(citations)
        sortkeys = sorted(cnt.keys(), reverse = True)
        cumulative = {}
        currcount, ret = 0, 0
        for ind, key in enumerate(sortkeys):
            precount = currcount
            currcount += cnt[sortkeys[ind]]
            cumulative[key] = currcount
            # case when h == key
            if precount <= key <= currcount:
                ret = max(ret, key)
            if ind == len(sortkeys)-1:
                if key >= len(citations):
                    ret = len(citations)
                break
            nextkey = sortkeys[ind+1]
            # case when h is between nextkey and current key
            if nextkey < currcount < key:
                ret = max(ret, currcount)
        return ret