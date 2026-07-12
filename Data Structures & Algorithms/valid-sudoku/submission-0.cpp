class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int len = board.size();
        // bool row = false;

        for(int i = 0; i < len; i++){
            unordered_set<char> container;
            for(int j = 0; j < len; j++){
                if(board[i][j] == '.' ){
                    continue;
                }else{
                    if(container.count(board[i][j])){
                        return false;
                    }
                    container.insert(board[i][j]);
                }
            }
        }

        for(int i = 0; i < len; i++){
            unordered_set<char> container;
            for(int j = 0; j < len; j++){
                if(board[j][i] == '.' ){
                    continue;
                }else{
                    if(container.count(board[j][i])){
                        return false;
                    }
                    container.insert(board[j][i]);
                }
            }
        }


        for(int r = 0; r < len ; r+=3){
            for(int c = 0; c < len ; c+=3){
                unordered_set<char> container;
                for(int i = r; i < r + 3; i++){
                    for(int j = c; j < c + 3; j++){
                        if(board[i][j] == '.' ){
                                continue;
                        }else{
                            if(container.count(board[i][j])){
                                return false;
                            }
                            container.insert(board[i][j]);
                        }
                }

                }
            }

        }


        return true;
    }
};
