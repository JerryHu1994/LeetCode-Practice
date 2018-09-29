class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right, dic, ret = 0, 0, collections.defaultdict(int), 0
        while right < len(s):
            while len(dic) == 2 and s[right] not in dic:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:   del dic[s[left]]
                left += 1
            dic[s[right]] += 1
            right += 1
            ret = max(ret, right-left)
            if right == len(s):   break
        return ret
        