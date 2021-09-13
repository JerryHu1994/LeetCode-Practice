class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        presum = []
        currsum = 0
        for num in arr:
            currsum += num
            presum.append(currsum)
        ans = 0
        for i in range(k-1, len(arr)):
            s = presum[i] - presum[i-k+1] + arr[i-k+1]
            if float(s)/k >= float(threshold):
                ans += 1
        return ans