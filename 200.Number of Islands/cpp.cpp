class Solution {
public:
    void dfs(vector<vector<char>>& grid, int x, int y, int height, int width) {
        queue<vector<int>> q;
        q.push({x, y});
        while (q.size()) {
            auto curr = q.front();
            q.pop();
            int currx = curr[0];
            int curry = curr[1];
            if (currx-1 >=0 && grid[curry][currx-1] == '1') {
                q.push({currx-1, curry});
                grid[curry][currx-1] = '2';
            }
            if (currx+1 < width && grid[curry][currx+1] == '1') {
                q.push({currx+1, curry});
                grid[curry][currx+1] = '2';
            }
            if (curry-1 >= 0 && grid[curry-1][currx] == '1') {
                q.push({currx, curry-1});
                grid[curry-1][currx] = '2';
            }
            if (curry+1 < height && grid[curry+1][currx] == '1') {
                q.push({currx, curry+1});
                grid[curry+1][currx] = '2';
            }
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0) {
            return 0;
        }
        int height = grid.size();
        int width = grid[0].size();
        int ret = 0;
        for(int i=0; i<height;i++){
            for (int j=0;j<width;j++){
                if (grid[i][j] == '1') {
                    dfs(grid, j, i, height, width);
                    ret +=1;
                }
            }
        }
        return ret;
        
    }
};