#ok
#ok
#include <bits/stdc++.h> 


using namespace std; 





int main() 
{ 
    ios_base::sync_with_stdio(0); 
    cin.tie(0); 
    #ifndef ONLINE_JUDGE 
        freopen("input.txt", "r", stdin); 
        freopen("output.txt", "w", stdout); 
    #endif  
       
    int t; 
    cin>>t;
    for(int i=1;i<=t;i++) 
    {
        int n,ans=0;
        cin>>n;
        vector<pair<int,int> > v;
        string s;
        cin>>s;
        //bool stX=false,stO=false;
        for(int i=1;i<n;i++)
        {
            if(s[i]!='F')
            {
                if(c!='F' && c!=s[i])dp[i]=dp[i-1]+1;
                else dp[i]=dp[i-1];
                // if(s[i]!='X')stX=true;
                // if(s[i]!='O')stO=true;
                c=s[i];
            }
            else dp[i]=dp[i-1];
        }
        //for(int i=0;i<n;i++)cout<<dp[i]<<" ";
        sm[0]=dp[0];
        for(int i=1;i<n;i++)sm[i]=sm[i-1]+dp[i];
        for(int i=0;i<n;i++)cout<<sm[i]<<" ";
        //cout<<"Case #"<<i<<": "<<ans;
        if(i<t)cout<<"\n";
    } 
    return 0; 
} 
    
