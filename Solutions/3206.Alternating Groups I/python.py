class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans, l = 0, len(colors)
        for i in range(l):
            curr, curr_next, curr_skip = i, (i+1)%l, (i+2)%l
            if colors[curr] != colors[curr_next] and colors[curr_next] != colors[curr_skip]:
                ans += 1
        return ans
            