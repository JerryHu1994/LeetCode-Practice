class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        slow, fast, currdic, ret = 0, 0, collections.defaultdict(int), 0
        while slow < len(tree):
            currlen = 0
            # keep moving fast until we have a third fruit
            while fast < len(tree) and len(currdic) <= 2:
                currdic[tree[fast]] += 1
                if len(currdic) <= 2:
                    currlen += 1
                    fast += 1
            ret = max(ret, fast-slow)
            if fast >= len(tree):   break
            # keep moving slow until we have only two fruits
            while len(currdic) > 2:
                currdic[tree[slow]] -= 1
                if currdic[tree[slow]] == 0:    del currdic[tree[slow]]
                slow += 1
            fast += 1
        return ret