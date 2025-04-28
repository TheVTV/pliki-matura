#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int sys_dec(string s, int sys){
    int ans=0;
    for(int i=s.size()-1; i>=0; i--){
        if(s[i]<='9'){
            ans+=(s[i]-'0')*pow(sys, s.size()-i-1);
        }
        else{
            ans+=(s[i]-'A'+10)*pow(sys, s.size()-i-1);
        }
    }

    return ans;
}

int low(string s){
    int dozw=1;
    for(char x : s){
        if(x<='9'){
            if(dozw<x-'0'){
                dozw=x-'0';
            }
        }
        else{
            if(dozw<x-'A'+10){
                dozw=x-'A'+10;
            }
        }
    }
    return dozw;
}

int main(){
    ifstream in("pliki/liczby.txt");
    ofstream out("wynik2.txt", ios::app);
    string s1, s2, w1, w2;
    int st;
    int minn=1e9, maxx=0;
    string minnn, maxxx;

    while(in >> s1 >> s2){
        st=max(low(s1), low(s2))+1;
        while(st<=16){
            w1=to_string(sys_dec(s1, st));
            w2=to_string(sys_dec(s2, st));
            reverse(w2.begin(), w2.end());
            if(w1==w2){
                if(minn>sys_dec(s1, st)){
                    minn=sys_dec(s1, st);
                    minnn=s1;
                }
                if(maxx<sys_dec(s1, st)){
                    maxx=sys_dec(s1, st);
                    maxxx=s1;
                }
                if(minn>sys_dec(s2, st)){
                    minn=sys_dec(s2, st);
                    minnn=s2;
                }
                if(maxx<sys_dec(s2, st)){
                    maxx=sys_dec(s2, st);
                    maxxx=s2;
                }
                break;
            }
            st++;
        }
    }


    out << "min: " << minnn << " max: " << maxxx;
    return 0;
}