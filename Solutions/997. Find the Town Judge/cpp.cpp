class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        unordered_map<int, vector<int>>graph;
        set<int> remain;
        for (int i=1;i<N+1;i++) remain.insert(i);
        for(int i=0;i<trust.size();i++){
            int from = trust[i][0];
            int to = trust[i][1];
            if (remain.find(from) != remain.end())  remain.erase(from);
            graph[to].push_back(from);
        }
        vector<int> ans;
        for (auto it=remain.begin(); it != remain.end(); ++it) {
            if (graph[*it].size() == N-1)   ans.push_back(*it);
        }
        return (ans.size() == 1) ? ans[0] : -1;
    }
};