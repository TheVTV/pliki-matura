#include<bits/stdc++.h>
using namespace std;

map <string,int> m;

string n(string c){
    string w="";
    for(int i=0;i<c.size();i++){
        if(c[i]=='0') w+='1';
        else w+='0';
    }
    return w;
}

string t(string s, int k){
    if(k==0) return s;
    string tt = t(s,k-1);
    string nn = n(tt);
    return tt+nn;
}

int main(){
    string s; int k;
    //cin>>s>>k;
  //  s="0"; k=4;
  //  string w = t(s,k);

   /* for(int i=0;i<w.size()-4;i++){
        string a = w.substr(i,4);
        if(m.count(a)) m[a]++;
        else m[a]=1;
    }

    cout<<m.size(); */

    s="0";

    for(k=1;k<1000;k++){
        string w = t(s,k);
        int il=0;
        for(int i=0;i<w.size();i++){
            if(w[i]=='1') il++;
        }
        if(il>=100){
            cout<<k;
            return 0;
        }
    }

}
