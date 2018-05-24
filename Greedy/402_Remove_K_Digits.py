'''

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

'''
class Solution {
public:
    string removeKdigits(string num, int k) {
                /*
        int n=num.length();
        
        if(k>=n)
            return "0";

        int start=INT_MAX;
        char c;
        for(int i=0;i<=k;i++){
            int temp=num[i]-'0';
            if(temp<start){
                start=temp;
                c=num[i];
                
            }
            
        }
        char *a=new char[n-k];
        a[0]=c;
        int j=0;
        if(c=='0'){
            for(int i=k+1;i<n;i++)
                a[j++]=num[i];
        }else{
             for(int i=k+1;i<n;i++)
                a[++j]=num[i];
        }
       
        return a; 
        
        
        char *stk=new char[n];
        int top=0,count=n-k;
        for(int i=0;i<n;i++){
            while(top!=0 && k>0 && stk[top-1]>num[i]){
                k--;
                top--;
            }
            stk[top++]=num[i];
        }
       
        int index=0;
        while(index<n-k &&stk[index]=='0')
            index++;
        if(index==count ){
            cout<<stk[0]<<endl;
            return "0";
        }
            
        //return index == n-k? "0": new String(stk, idx, digits - idx);
        else{
              char *a=new char[n];
        int j=0;
        for(int i=index;i<n-k;i++)
            a[j++]=stk[i];
        return a;
        }
      */
        int n = num.length(), remain = n - k;
        if(remain == 0) return "0";
        string s = "";
        for(auto x: num){
            while(n > remain && !s.empty() && s.back() - '0' > x - '0'){
                s.pop_back();
                n--;
            }
            s.push_back(x);
        }
        int i = 0;
        while(i < s.size() && s[i] == '0') i++;
        return s.substr(i, remain) == "" ? "0" : s.substr(i, remain);
    
        
        
        
    }
};

