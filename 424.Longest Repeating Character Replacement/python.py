class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left, right, dic, ret = 0, 0, collections.defaultdict(int), 0
        while right < len(s):
            while True:
                vals = dic.values()
                if len(vals) == 0 or max(vals) == 0:  break
                currbest = max(dic.values())
                currtotal = right - left
                bestkeys = [key for key, v in dic.iteritems() if v == currbest]
                if not (currtotal-currbest == k and s[right] not in bestkeys):  break
                dic[s[left]] -= 1
                left += 1
            dic[s[right]] += 1
            right += 1
            ret = max(ret, right-left)
            if right == len(s): break
        return ret