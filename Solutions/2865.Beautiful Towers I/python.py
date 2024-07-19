class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        ans = 0
        for i in range(len(maxHeights)):
            currsum = maxHeights[i]
            curr = maxHeights[i]
            for j in range(i-1,-1, -1):
                curr = maxHeights[j] if maxHeights[j] <= curr else curr
                currsum += curr
            curr = maxHeights[i]
            for k in range(i+1, len(maxHeights)):
                curr = maxHeights[k] if maxHeights[k] <= curr else curr
                currsum += curr
            ans = max(ans, currsum)
        return ans