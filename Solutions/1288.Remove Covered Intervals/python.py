class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        times = [(i[0], -i[1]) for i in intervals]
        times = sorted(times)
        ans = 0
        curr_left, curr_right = times[0][0], -times[0][1]
        for left, right in times[1:]:
            l, r = left, -right
            if curr_left <= l and r <= curr_right:
                continue
            else:
                curr_left, curr_right = l, r
                ans += 1
        ans += 1
        return ans