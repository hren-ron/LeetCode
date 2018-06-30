'''

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
'''


class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        
        int n=nums.size();
        
        if(n<=1)
            return nums;
        //nums=quicksort(nums,0,n-1);
        //sort(nums.begin(),nums.end(),greater<int>());
        sort(nums.begin(),nums.end());
        //int *dp=new int[n];
        vector<int> dp(n,1);
        vector<int> parent(n,-1);
        
        int maxSize=1,maxi=0;
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(nums[i]%nums[j]==0 && dp[j]+1>dp[i]){
                    dp[i]=dp[j]+1;
                    parent[i]=j;
                }
                    
                if(dp[i]>maxSize){
                    maxSize=dp[i];
                    maxi=i;
                }
                
            }
        }
        
        cout<<maxSize<<maxi<<endl;;
        
        for(int i=0;i<n;i++)
            cout<<parent[i]<<endl;
        
        vector<int> res;
        
        while(maxSize--){
            res.push_back(nums[maxi]);
            maxi=parent[maxi];
        }
        
        return res;
        
    }
    
    
    bool compare(int a,int b){
        return a>b;
    }
    vector<int> quicksort(vector<int> ns,int start,int end){
        int pivotpos=partition(ns,start,end);
        quicksort(ns,start,pivotpos-1);
        quicksort(ns,pivotpos+1,end);
        return ns;
    }
    
    int partition(vector<int> ns,int left,int right){
        int pivotpos=left,pivot=ns[left];
        
        for(int i=left+1;i<=right;i++){
            if(ns[i]<pivot){
                pivotpos++;
                int temp=ns[pivotpos];
                ns[pivotpos]=ns[i];
                ns[i]=temp;
            }
        }
        ns[left]=ns[pivotpos];
        ns[pivotpos]=pivot;
        return pivotpos;
        
    }
};