class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # form pairs
        dic = collections.defaultdict(list)
        for ind, val in enumerate(S):
            dic[val].append(ind)
        currstart, currs, ret = 0, set(), []
        for ind, val in enumerate(S):
            if val in currs:
                if ind == dic[val][-1]:
                    currs.remove(val)
            elif len(dic[val])!=1:
                currs.add(val)
            # set is empty, create a parition
            if len(currs) == 0:
                ret.append(ind - currstart + 1)
                currstart = ind + 1
        return ret