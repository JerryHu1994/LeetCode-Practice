class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        sorted_env = sorted(envelopes, key = lambda x:[x[0], -x[1]])
        taillist = []
        heights = [i[1] for i in sorted_env]
        for ind, env in enumerate(heights):
            # each time append idx or replace idx according to bisect
            insert_idx = bisect.bisect_left(taillist, env)
            if insert_idx == len(taillist):
                taillist.append(env)
            else:
                taillist[insert_idx] = env
        return len(taillist)