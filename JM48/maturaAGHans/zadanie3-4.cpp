#include <iostream>
#include <fstream>

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

bool check(int n){
    int ans=0;
    for(int i=1; i<n; i++){
        if(n%i==0){
            ans+=i;
        }
    }
    if(ans==n){
        return true;
    }
    return false;
}

int main(){
    ifstream in("pliki/kebab.txt");
    ofstream out("wyniki3.txt", ios::app);
    int n, prev, cur, ile, liczba, ans=0;
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
        if(check(liczba)){
            ans++;
        }
    }

    out << ans;

    return 0;
}