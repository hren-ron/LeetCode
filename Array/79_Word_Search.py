'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''


class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        /*
        使用深度优先搜索的方法，使用等大小的数组，记录是否访问过
        */
        
        int m=board.size(),n=board[0].size();
        if(word.length()==0) return true;
        if(m==0 || n==0) return false;
        vector<vector<char>> visit(m,vector<char>(n,false));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(board[i][j]==word[0])
                    if(dfs(board,word,visit,i,j,0)) return true;
            }
        }
        return false;
    }
    bool dfs(vector<vector<char>> &board,string word,vector<vector<char>> &visit,int row,int col,int count){
        if(count==word.length()-1) return true;
        visit[row][col]=true;
        if(row+1<board.size() && visit[row+1][col]==false && word[count+1]==board[row+1][col]){
            if(dfs(board,word,visit,row+1,col,count+1)) return true;
        }
        if(row-1>=0 && visit[row-1][col]==false && word[count+1]==board[row-1][col]){
            if(dfs(board,word,visit,row-1,col,count+1)) return true;
        }
        if(col+1<board[0].size() && visit[row][col+1]==false && word[count+1]==board[row][col+1]){
            if(dfs(board,word,visit,row,col+1,count+1)) return true;
        }
        if(col-1>=0 && visit[row][col-1]==false && word[count+1]==board[row][col-1]){
            if(dfs(board,word,visit,row,col-1,count+1)) return true;
        }
        visit[row][col]=false;
        return false;
    }
};
