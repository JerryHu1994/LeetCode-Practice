class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = defaultdict(int)
        for num in nums:    cnt[num] += 1
        ans = 0
        for num in nums:
            currlen = len(num)
            if target[0:currlen] == num:
                if target[currlen:] in cnt:
                    if target[currlen:] != num:
                        ans += cnt[target[currlen:]]
                    else:
                        ans += cnt[target[currlen:]] - 1
        return ans