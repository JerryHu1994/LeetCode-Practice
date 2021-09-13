class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if not len(A):  return []
        curr_cnt = collections.Counter(A[0])
        for string in A[1:]:
            cnt = collections.Counter(string)
            keys = [k for k in curr_cnt.keys()] + [k for k in cnt.keys()]
            next_cnt = {}
            for k in keys:
                if k in curr_cnt and k in cnt:
                    next_cnt[k] = min(curr_cnt[k], cnt[k])
            curr_cnt = next_cnt
        ans = []
        for k in curr_cnt:  ans.extend([k]*curr_cnt[k])
        return ans