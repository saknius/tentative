class Solution {
public:
    int n;
    vector <int> v;
    int dp[110][110];
    int sum[100];
    int fun(int i,int m)
    {
        if(i==v.size())
        return 0;
        if(2*m>=v.size()-i)
        return sum[i];    
        if(dp[i][m]!=-1)
        return dp[i][m];
        int mn=INT_MAX;
        for(int j=1;j<=2*m;j++)
        mn=min(mn,fun(i+j,max(j,m)));
        return dp[i][m]=sum[i]-mn;
    }
    int stoneGameII(vector<int>& piles) {
       sum[piles.size()-1]=piles[piles.size()-1];
       n=piles.size();
       for(int i=n-2;i>=0;i--)
       sum[i]=sum[i+1]+piles[i];
       v=piles;
        for(int i=0;i<110;i++)
        {
            for(int j=0;j<110;j++)
                dp[i][j]=-1;
        }
       return fun(0,1); 
    }
};