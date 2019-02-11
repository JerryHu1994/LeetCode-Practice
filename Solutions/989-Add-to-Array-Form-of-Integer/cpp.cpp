class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
        vector<int> res;
        int sum = 0, carry = 0;
        for (int i=A.size()-1; i>=0;i--) {
            sum = A[i] + (K%10) + carry;
            res.push_back(sum%10);
            carry = sum/10;
            K/=10;
        }
        K += carry;
        while (K>0) {
            res.push_back(K%10);
            K = K/10;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};