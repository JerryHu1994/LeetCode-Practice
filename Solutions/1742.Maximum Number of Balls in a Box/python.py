class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = defaultdict(int)
        for num in range(lowLimit, highLimit+1):
            currsum = sum([int(i) for i in str(num)])
            dic[currsum] += 1
        ans = 0
        for k, v in dic.items():
            if v > ans:
                ans = v
        return ans
                