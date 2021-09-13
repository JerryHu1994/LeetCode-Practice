class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        presum = []
        curr_sum = 0
        for num in arr:
            curr_sum += num
            presum.append(curr_sum)
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j-i+1) % 2 == 1:
                    ans += presum[j] - presum[i] + arr[i]
        return ans
        