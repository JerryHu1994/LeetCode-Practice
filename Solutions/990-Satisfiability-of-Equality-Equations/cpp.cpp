class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        vector<string>equallist;
        vector<string>notequallist;
        for (int i=0;i<equations.size();i++){
            if (equations[i].find("!=") == string::npos) {
                equallist.push_back(equations[i]);
            } else {
                notequallist.push_back(equations[i]);
            }
        }
        // add every pair into graph
        unordered_map<string, vector<string>> graph;
        for (string s : equallist) {
            string first = s.substr(0, 1);
            string second = s.substr(3, 1);
            graph[first].push_back(second);
            graph[second].push_back(first);
        }
        for (string s : notequallist) {
            string first = s.substr(0, 1);
            string second = s.substr(3, 1);
            set<string> visited;
            visited.insert(first);
            if (dfs(first, second, visited, graph))    return false;
        }
        return true;
    }
private:
    bool dfs(string start, string end, set<string> visited, unordered_map<string, vector<string>>graph) {
        if (start.compare(end) == 0)  return true;
        for (string next : graph[start]) {
            if (visited.find(next) == visited.end()) {
                visited.insert(next);
                bool ret = dfs(next, end, visited, graph);
                if (ret) {return true;}
                visited.erase(next);
            }
        }
        return false;
    }
};