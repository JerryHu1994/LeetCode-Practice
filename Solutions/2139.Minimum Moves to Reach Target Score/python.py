class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        double_cnt = 0
        curr = target
        ans = 0
        while curr > 1:
            if maxDoubles == 0:
                ans += int(curr) - 1
                break
            if curr % 2 == 1:
                curr -= 1
            else:
                curr /= 2
                maxDoubles -= 1
            ans += 1
        return ans
                