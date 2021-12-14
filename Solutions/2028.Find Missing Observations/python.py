class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_sum = (len(rolls)+n)*mean
        remain_sum = total_sum - sum(rolls)
        if remain_sum > n*6 or remain_sum < n:
            return []
        div = remain_sum // n
        extra = remain_sum - div*n 
        ans = []
        for i in range(n):
            ans.append(div+1 if i < extra else div)
        return ans