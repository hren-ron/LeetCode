'''
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
'''

class Solution {
public:
    string pushDominoes(string dominoes) {
        
        int n=dominoes.length();
        int *dp=new int[n+2];
        
        char *s=new char[n+2];
        
        dp[0]=-1;
        s[0]='L';
        int index=1;
        for(int i=0;i<n;i++){
            if(dominoes[i]!='.'){
                dp[index]=i;
                s[index++]=dominoes[i];
            }
        }
        
        dp[index]=n;
        s[index++]='R';
        
        
        for(int i=0;i<index-1;i++){
            
            int i1=dp[i],j=dp[i+1];
            char x=s[i],y=s[i+1];
            if(x==y){
                for(int k=i1+1;k<j;k++){
                    dominoes[k]=x;
                }
            }else if(x>y){
                for(int k=i1+1;k<j;k++){
                
                    dominoes[k]=k-i1==j-k?'.':k-i1<j-k?'R':'L';
                }
            }
            
        }
        return dominoes;
    }
};
