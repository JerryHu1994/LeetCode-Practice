class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        currmax = 0
        n = len(nums)
        sur_max_list = []
        for num in nums[::-1]:
            currmax = max(num, currmax)
            sur_max_list.append(currmax)
        sur_max_list = sur_max_list[::-1]
        currmax = 0
        pre_max_list = []
        for num in nums:
            currmax = max(currmax, num)
            pre_max_list.append(currmax)
        ans = 0
        for j in range(1, n-1):
            if pre_max_list[j-1] > nums[j]:
                ans = max(ans, (pre_max_list[j-1]-nums[j])*sur_max_list[j+1])
        return ans