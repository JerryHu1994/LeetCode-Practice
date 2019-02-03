class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(string s : strs){
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            if (map.find(sorted) == map.end()) {
                vector<string> newvector;
                newvector.push_back(s);
                map[sorted] = newvector;
            } else {
                map[sorted].push_back(s);
            }
        }
        vector<vector<string>> ret;
        for (auto itr : map) {
            ret.push_back(itr.second);
        }
        return ret;
    }
};