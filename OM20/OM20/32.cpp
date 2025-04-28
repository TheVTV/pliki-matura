#include<bits/stdc++.h>
using namespace std;

int ilp, ilf;

bool pierw(int n){
    if(n<2) return false;
    if(n==2) return true;
    if(n%2==0) return false;
    for(int i=3;i<n;i++) if(n%i==0) return false;
    return true;
}

bool palind(int n){
    string a = to_string(n);
    string b = "";
    for(int i=0;i<a.size();i++) b=a[i]+b;
    if(a==b) return true;
    return false;
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
            int keb=0;
        //int il=0;
        int n =x;
        while(1){
            keb+=n;
            n = roz(n);

            if(pierw(n)){
                //il+=2;
                keb=keb+n+n;

                if(palind(keb)) ilp++;
                if(pierw(keb)) ilf++;

                break;
            }

           // il++;


        }
    }

   cout<<ilp<<" "<<ilf;


}

