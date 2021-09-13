class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        int rooky = 0, rookx = 0;
        for (int i=0; i<8; i++) {
            for (int j=0; j<8; j++) {
                if (board[i][j] == 'R') {
                    rooky = i;
                    rookx = j;
                    break;
                }
            }
        }
        int dirx[4] = {1, -1, 0, 0};
        int diry[4] = {0, 0, 1, -1};
        int ans = 0;
        for (int i=0; i<4; i++) {
            int dx = dirx[i];
            int dy = diry[i];
            int currx = rookx+dx;
            int curry = rooky+dy;
            while (currx >= 0 && currx < 8 && curry >= 0 && curry < 8 && board[curry][currx] != 'B') {
                if (board[curry][currx] == 'p') {
                    ans+=1;
                    break;
                }
                currx += dx;
                curry += dy;
            }
        }
        return ans;
    }
};