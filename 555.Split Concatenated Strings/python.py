class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strings = [s if s > s[::-1] else s[::-1] for s in strs]
        ans = ""
        for ind, val in enumerate(strings):
            between = "".join(strings[ind+1:] + strings[:ind])
            for w in (val, val[::-1]):
                for start in range(len(w)):
                    curr_string = w[start:] + between + w[:start]
                    if curr_string > ans:
                        ans = curr_string
        return ans
                