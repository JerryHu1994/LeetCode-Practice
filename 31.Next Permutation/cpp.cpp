class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int s = int(nums.size());
        if (s < 2) return;   
        int ind = s-1;
        while (ind > 0 && nums[ind] <= nums[ind-1]) ind -= 1;
        if (ind == 0) {
            sort(nums.begin(), nums.end());
            return;
        }
        int front = ind-1;
        int val = nums[front];
        while (ind < s-1 && !(nums[ind] > val && nums[ind+1] <= val))   ind++;
        nums[front] = nums[ind];
        nums[ind] = val;
        vector<int>temp;
        for (int i=s-1;i>front;i--) temp.push_back(nums[i]);
        for (int i=front+1;i<s;i++) nums[i] = temp[i-front-1];
        return;
    }
};