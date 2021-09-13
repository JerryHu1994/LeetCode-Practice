class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        dic = defaultdict(list)
        for k in cnt:
            dic[cnt[k]].append(k)
        keys = []
        for k in dic:   
            keys.append(k)
            dic[k] = sorted(dic[k], reverse = True)
        keys = sorted(keys)
        ans = []
        for k in keys:
            for char in dic[k]:
                ans += [char]*k
        return ans
        