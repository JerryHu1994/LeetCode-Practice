class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int s = int(nums.size());
        sort(nums.begin(), nums.end());
        vector<vector<int>>ret;
        for (int i=0; i < s-2; i++){
            if (nums[i]==nums[i-1] && i != 0) continue;
            int target = 0 - nums[i];
            int left = i+1, right = s-1;
            while (left < right) {
                if (nums[left] + nums[right] > target) {
                    right--;
                } else if (nums[left] + nums[right] < target) {
                    left++;
                } else {
                    vector<int> valid = {nums[i], nums[left], nums[right]};
                    ret.push_back(valid);
                    left ++;
                    right --;
                    while (left < s and nums[left]==nums[left-1]) left += 1;
                    while (right >= 0 and nums[right]==nums[right+1]) right -= 1;
                }
            }
        }
        return ret;
    }
};