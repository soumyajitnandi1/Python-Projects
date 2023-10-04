#include<iostream>
#include<vector>
using namespace std;

//60=2^2*3*5 
//no of divisors=(2+1)*(1+1)*(1+1)=12

int factors(int n){
    int res=1;
    for (int i=2; i*i<=n; i++){
        int count=0;
        if(n%i==0){
            while(n%i==0){
                n=n/i;
                count+=1;
            }
            res=res*(count+1);
        }
    }
    if(n!=1){
        res*=2;
    }
    return res;
}

//FOR IO
int main(){
    int n;
    cin>>n;
    cout<<factors(n);
    return 0;
}
