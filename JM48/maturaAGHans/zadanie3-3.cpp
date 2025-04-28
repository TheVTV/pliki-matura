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
    int n, prev, cur, ile, liczba, par=0, npar=0, ans=0;
    while(in >> n){
        par=0;
        npar=0;
        liczba=n;
        prev=-1;
        ile=2;
        cur=n;
        if(n%2==0){
            par++;
        }
        else{
            npar++;
        }
        while(prev!=skladanie(cur)){
            if(skladanie(cur)%2==0){
                par++;
            }
            else{
                npar++;
            }
            prev=skladanie(cur);
            liczba+=skladanie(cur);
            cur=skladanie(cur);
            ile++;
        }
        liczba+=prev;
        if(prev%2==0){
            par++;
        }
        else{
            npar++;
        }
        if(npar==par){
            ans++;
        }
    }

    out << ans;

    return 0;
}