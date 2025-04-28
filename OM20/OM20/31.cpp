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

int ilmax=0, nmax;

int main(){
    ifstream od ("kebab_przyklad.txt");

    int n;
    while(od>>n){
        int il=0;
        int x=n;
        while(1){
            il++;
            int x = roz(x);
            if(pierw(x)){
                il+=2;
                if(il>ilmax){
                    ilmax=il;
                    nmax= n;
                    break;
                }
            }
        }
    }

    cout<<ilmax<<endl<<nmax;
}
