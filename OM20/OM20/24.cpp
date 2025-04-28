#include<bits/stdc++.h>
using namespace std;

int main(){
    ifstream od ("liczby.txt");

    map <char,int> m;

    int il=0;

    string s;
    while(od>>s){
            il+=s.size();
        for(int i=0;i<s.size();i++){
           // il++;
            char x = s[i];
            if(m.count(x)) m[x]++;
            else m[x]=1;
        }
    }


    for(char i='0';i<='9';i++){
        cout<<i<<" "<<fixed<<setprecision(2)<< (double)((double)m[i]/(double)il)*100<<endl;
    }
    for(char i='A';i<='F';i++) cout<<i<<" "<<fixed<<setprecision(2)<< (double)((double)m[i]/(double)il)*100<<endl;
}
