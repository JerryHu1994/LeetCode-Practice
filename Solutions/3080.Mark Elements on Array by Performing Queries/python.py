class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(nums)
        ans = []
        mark_map = [False]*len(nums)
        cnt = set(nums)
        hq = []
        for ind, num in enumerate(nums):
            heapq.heappush(hq, (num,ind))
        for ind, nsmallest in queries:
            if not mark_map[ind]:
                s -= nums[ind]
                mark_map[ind] = True
            smallestcnt = 0
            while len(hq) and smallestcnt < nsmallest:
                currval, currind = heapq.heappop(hq)
                if mark_map[currind]:   continue
                s -= nums[currind]
                mark_map[currind] = True
                smallestcnt += 1
            ans.append(s)
        return ans