class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_candles = [-1]*n
        suffix_candles = [n]*n
        pre_candle_pos = -1
        for ind in range(n):
            if s[ind] == '|':
                pre_candle_pos = ind
            prefix_candles[ind] = pre_candle_pos
        next_candle_pos = n
        for ind in range(n-1, -1, -1):
            if s[ind] == '|':
                next_candle_pos = ind
            suffix_candles[ind] = next_candle_pos
        prefix_plate_count = []
        curr_cnt = 0
        for ele in s:
            if ele == '*':
                curr_cnt += 1
            prefix_plate_count.append(curr_cnt)
        
        ans = []
        for startind, endind in queries:
            if suffix_candles[startind] > endind or prefix_candles[endind] <  startind:
                ans.append(0)
            elif suffix_candles[startind] > n-1 or prefix_candles[endind] < 0:
                ans.append(0)
            else:
                ans.append(prefix_plate_count[prefix_candles[endind]] - prefix_plate_count[suffix_candles[startind]])
        return ans