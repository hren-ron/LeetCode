'''

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        
        /*
        用hashmap保存A和B的和即对应次数的关系，即key为A元素B元素的和，value为对应元素的和的次数，那么在遍历C和D时，只需要寻找A和B和的相反数即可，累加到res中。
        */
        
        
        unordered_map<int,int>map1,map2;
        int n=A.size(),res=0;
        
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                map1[A[i]+B[j]]++;
            }
        
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                int temp=(-1)*(C[i]+D[j]);
                res+=map1[temp];
            }          
        return res;
    }
};


