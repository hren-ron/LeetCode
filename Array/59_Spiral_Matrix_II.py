'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        
        vector<vector<int>> res(n,vector<int>(n));
        
        int left=0,right=n-1,up=0,down=n-1,num=1;
        
        while(true){
            for(int i=left;i<=right;i++) res[up][i]=num++;
            
            if(++up>down) break;
            
            for(int i=up;i<=down;i++) res[i][right]=num++;
            if(--right<left) break;
            
            for(int i=right;i>=left;i--) res[down][i]=num++;
            if(--down<up) break;
            
            for(int i=down;i>=up;i--) res[i][left]=num++;
            if(++left>right) break;
            
        }
        return res;
        
    }
};