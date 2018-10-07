class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int>cnt;
        for (int i : deck)  cnt[i] += 1;
        vector<int> values, divs;
        for (auto &it : cnt)    values.push_back(it.second);
        int min_ele = *min_element(values.begin(), values.end());
        for (int i = 2;i<=min_ele;i++) {
            if (min_ele%i == 0) divs.push_back(i);
        }
        for (int i : divs) {
            bool valid = true;
            for (int v : values) {
                if (v%i != 0) {
                    valid = false;
                    break;
                }
            }
            if (valid)  return true;
        }
        return false;
    }
};