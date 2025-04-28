#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int skladanie(int n){
    int ans=0;
    int cur=2;
    while(n!=1){
        if(n%cur==0){
            ans+=cur;
            n/=cur;
        }
        else{
            cur++;
        }
    }

    return ans;
}

int main(){
    ifstream in("pliki/kebab.txt");
    ofstream out("wyniki3.txt", ios::app);
    int n, prev, cur, ile, liczba, maxx=0;
    vector<int> v;

    while(in >> n){
        liczba=n;
        prev=-1;
        ile=2;
        cur=n;
        while(prev!=skladanie(cur)){
            prev=skladanie(cur);
            liczba+=skladanie(cur);
            cur=skladanie(cur);
            ile++;
        }
        liczba+=prev;
        if(maxx==ile){
            v.push_back(n);
        }
        else if(maxx<ile){
            maxx=ile;
            v.clear();
            v.push_back(n);
        }
    }
    out << maxx << '\n';
    for(int x : v){
        out << x << '\n';
    }

    return 0;
}