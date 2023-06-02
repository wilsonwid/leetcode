class Solution {
public:
    bool inference(vector<vector<char>>& board, int i, int j) {
        if (i == 9) return true;
        int jNext = (j+1)%9;
        int iNext = j == 8 ? i+1 : i;

        if (board[i][j] != '.') return inference(board, iNext, jNext);
        else {
            for (char num = '1'; num <= '9'; num++) {
                // check for clashes
                bool clash = false;

                for (int col = 0; col < 9; col++) {
                    if (board[i][col] == num) {
                        clash = true;
                        break;
                    }
                }

                if (clash) continue;

                for (int row = 0; row < 9; row++) {
                    if (board[row][j] == num) {
                        clash = true;
                        break;
                    }
                }

                if (clash) continue;
                int curGridRow = i/3;
                int curGridCol = j/3;
                
                for (int row = curGridRow*3; row < curGridRow*3+3; row++) {
                    if (clash) break;
                    for (int col = curGridCol*3; col < curGridCol*3+3; col++) {
                        if (board[row][col] == num) {
                            clash = true;
                            break;
                        }
                    }
                }

                if (clash) continue;

                board[i][j] = num;
                if (inference(board, iNext, jNext)) return true;
                board[i][j] = '.';
            }
            return false;
        }
    }

    void solveSudoku(vector<vector<char>>& board) {
        inference(board, 0, 0);
    }
};
