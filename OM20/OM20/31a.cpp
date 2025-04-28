#include<bits/stdc++.h>
using namespace std;

bool pierw(int n){
    if(n<2) return false;
    if(n==2) return true;
    if(n%2==0) return false;
    for(int i=3;i<n;i++) if(n%i==0) return false;
    return true;
}

int roz(int n){  //suma liczb z rozkładu
    int s=0;
    int i=2;
    while(n>1){
        while(n%i==0){
            s+=i;
            n/=i;
        }
        i++;
        while(!pierw(i)) i++;
    }
    return s;
}

int main(){
    ifstream od ("kebab.txt");

    vector <int> v;

    int x;
    int ilmax=0;
    while(od>>x){
        int il=0;
        int n =x;
        while(1){
            if(pierw(n)){
                il+=2;
                if(il==ilmax) v.push_back(x);
                if(il>ilmax){
                    ilmax=il;
                    v.clear();
                    v.push_back(x);
                }
                break;
            }

            il++;
             n = roz(n);

        }
    }

    cout<<ilmax<<endl;

    for(int i=0;i<v.size();i++) cout<<v[i]<<endl;


}
