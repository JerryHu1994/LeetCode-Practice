class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        sorted_pairs = []
        for (start, end, height) in buildings:
            sorted_pairs.append((start, height))
            sorted_pairs.append((end, -height))
        sorted_pairs = sorted(sorted_pairs)
        currcnt, currsum, prev = 0, 0, None
        ans = []
        for pos, height in sorted_pairs:
            if prev != pos and currcnt > 0:
                avg = currsum // currcnt
                if ans and ans[-1][-1] == avg and ans[-1][1] == prev:
                    ans[-1][-2] = pos
                else:
                    ans.append([prev, pos, avg])
            prev = pos
            currcnt += 1 if height > 0 else -1
            currsum += height
        return ans