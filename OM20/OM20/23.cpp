#include<bits/stdc++.h>
using namespace std;

int horner (string l, int system)
{
    int i,y;
    if(l[0]<65)
        y=l[0]-48;
    else
        y=l[0]-55;

    for(i=1;i<l.size();i++)
    {
        if(l[i]<65)
            y=y*system+l[i]-48;
        else
            y=y*system+l[i]-55;
    }
    return y;
}

bool same(int a, int b){
    string x = to_string(a);
    string y = to_string(b);
    string z ="";
    for(int i=0;i<x.size();i++) z=x[i]+z;
    if(z==y) return true;
    return false;
}

int main(){
    ifstream od ("liczby.txt");

    string a,b;

    vector <int> v;
    v.resize(17,0);

    int ilmax=0, ilmin=100000;
    string big, small;

    while(od>>a>>b){
        for(int i=2;i<=16;i++){
            int x = horner(a,i);
            int y = horner(b,i);
            if(same(x,y)){
                if(x>ilmax) {ilmax=x; big=a;}
                if(y>ilmax) {ilmax=y; big=b;}
                if(x<ilmin) {ilmin=x; small=a;}
                if(y<ilmin) {ilmin=y; small=b;}
                break;
            }
        }
    }

    cout<<big<<" "<<small;
}
