class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        int left = 0, right = A.size()-1;
        vector<int> ans;
        while (left <= right) {
            if (abs(A[left]) >= abs(A[right])) {
                ans.push_back(pow(A[left], 2));
                left += 1;
            } else {
                ans.push_back(pow(A[right], 2));
                right -= 1;
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};