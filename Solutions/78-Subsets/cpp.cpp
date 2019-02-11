class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> curr;
        for (int i=0; i <= nums.size(); i++) {
            dfs(nums, i, 0, curr, ans);
        }
        return ans;
    }
    
private:
    void dfs(const vector<int> & nums, int n, int start, vector<int>& curr, vector<vector<int>>& ans) {
        if (n == curr.size()) {
            ans.push_back(curr);
            return;
        }
        for (int j = start; j < nums.size(); j++) {
            curr.push_back(nums[j]);
            dfs(nums, n, j+1, curr, ans);
            curr.pop_back();
        }
    }
};