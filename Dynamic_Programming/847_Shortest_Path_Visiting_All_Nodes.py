'''

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length
'''

class Solution {
public:
    int dp[1<<12][12];
    int dist[12][12] ; 
    void floyd( vector< vector< int> > & graph ){
        int n = graph.size(); 
        
        for( int i =0 ; i < n; i++)
            for( int j =0 ; j<n ; j++)
                dist[i][j] = n*n ; 
            
        
        for( int i  =0 ; i< n; i ++)
            dist[i][i] = 0 ; 
        
        for( int u = 0 ; u<n ; u++)
            for( auto & v : graph[u] ){
                dist[u][v] = 1 ;
                dist[v][u] = 1; 
            }
        
        
            for( int k =0 ; k< n ;k++)
                for( int i =0 ; i<n ; i++)
                    for( int j=0 ; j<n ; j++)
                        if( k!=i && k!=j )
                            dist[i][j] = min( dist[i][j] , dist[i][k] +dist[k][j] );   
            
        
    }
    int shortestPathLength(vector<vector<int>>& graph) {
        int n = graph.size() ; 
        floyd( graph ) ; 
        for( int i=0 ; i< n ; i++)
            for( int j=0 ; j<( 1<<n ) ; j++)
                dp[j][i] = n*n; 
            
        
        for( int i=0 ; i< n; i++)
            dp[1<<i][i] = 0 ; 
        
        for( int j=1 ; j<(1<<n) ;  j++)
            for(int i=0;i<n ;i++)
                if( j &(1<<i) ) 
                    for( int k=0 ;k<n ;k++)
                        dp[j][i] = min( dp[j][i] , dp[j^(1<<i)][k]+dist[k][i] ) ; 
                   
        int res = 1<< 15 ; 
        for( int i=0 ; i< n; i++){
            res = min ( res , dp[(1<<n) -1][i] ) ; 
        }
        return res; 
    }
};
