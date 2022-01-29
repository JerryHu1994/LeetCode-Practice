class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        hp = [-n for n in nums]
        heapq.heapify(hp)
        cnt = defaultdict(int)
        for i in range(k):
            cnt[heapq.heappop(hp)] += 1
        ans = []
        for n in nums:
            if -n in cnt:
                ans.append(n)
                cnt[-n] -= 1
                if cnt[-n] == 0: del cnt[-n]
        return ans
        
        
        