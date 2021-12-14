class Solution:
    def numSplits(self, s: str) -> int:
        dic = defaultdict(list)
        set_front = set()
        for ind, val in enumerate(s[:-1]):
            set_front.add(val)
            dic[ind].append(len(set_front))
        set_back = set()
        for ind, val in enumerate(s[::-1][:-1]):
            set_back.add(val)
            dic[len(s)-2-ind].append(len(set_back))
        ans = 0
        for key, val in dic.items():
            if val[0] == val[1]:    ans += 1
        return ans