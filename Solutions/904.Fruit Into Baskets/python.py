class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        dic, ret = collections.defaultdict(int), 0
        left, right = 0, 0
        while right < len(tree):
            # advance the right
            dic[tree[right]] += 1
            right += 1
            if len(dic) <= 2:   ret = max(right-left, ret)
            while len(dic) > 2:
                dic[tree[left]] -= 1
                if dic[tree[left]] == 0:    del dic[tree[left]]
                left += 1
        return ret