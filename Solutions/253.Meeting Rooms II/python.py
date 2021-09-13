class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))
        times = sorted(times)
        ans = 0
        curr = 0
        for timestamp, sign in times:
            if sign == 1:
                curr += 1
                ans = max(curr, ans)
            else:
                curr -= 1
        return ans