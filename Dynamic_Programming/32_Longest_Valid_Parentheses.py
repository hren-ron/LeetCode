'''

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution {
public:
    int longestValidParentheses(string s) {
        
        int n=s.length(),m=0;
        int *a=new int[n];
        for(int i=0;i<n;i++)
            a[i]=0;
        for(int i=1;i<n;i++){
            if(s[i]==')' && s[i-1]=='(')
                a[i]=(i>=2?a[i-2]:0)+2;
            else{
                if(s[i]==')' && s[i-1]==')'){
                    if(s[i-1-a[i-1]]=='(')
                        a[i]=a[i-1]+2+a[i-a[i-1]-2];
                }
            }
            m=max(m,a[i]);
                
        }
        return m;
        
    }
};
