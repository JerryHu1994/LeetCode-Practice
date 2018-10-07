class Solution {
public:
    int partitionDisjoint(vector<int>& A) {
        int leftmax = INT_MIN;
        int rightmin = INT_MAX;
        vector<int>maxlist, minlist;
        for (int i=0; i<A.size(); i++) {
            leftmax = max(leftmax, A[i]);
            rightmin = min(rightmin, A[A.size()-1-i]);
            maxlist.push_back(leftmax);
            minlist.push_back(rightmin);
        }
        reverse(minlist.begin(), minlist.end());
        for (int j=0; j<A.size()-1; j++) {
            if (maxlist[j] <= minlist[j+1]) {
                return j+1;
            }
        }
        return A.size();
    }
};