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

bool pr(int n){
    if(n%2==0){
        return false;
    }
    if(n==1){
        return false;
    }
    for(int i=3; i<=sqrt(n); i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    ifstream in("pliki/kebab.txt");
    ofstream out("wyniki3.txt", ios::app);
    int n, prev, cur, ile, liczba, prime=0, pali=0;
    string s;
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
        if(pr(liczba)){
            prime++;
        }
        s=to_string(liczba);
        reverse(s.begin(), s.end());
        if(to_string(liczba)==s){
            pali++;
        }
    }
    out << pali << ' ' << prime;

    return 0;
}