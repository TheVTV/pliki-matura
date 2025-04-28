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

    int il=0;


    int x;
    while(od>>x){
        int n =x;
        int ilp=0, iln=0;
        while(1){
            if(n%2==0) ilp++; else iln++;
             n = roz(n);
            if(pierw(n)){
                if(n%2==0) ilp+=2; else iln+=2;
                if(ilp==iln) il++;
                break;
            }


        }
    }


    cout<<il;


}

