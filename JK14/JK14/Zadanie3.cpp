#include <bits/stdc++.h>
using namespace std;


bool czy_pierwsza(int liczba){
    if(liczba==1)
        return false;
    if(liczba==2)
        return true;
    for(int i=2;i<=sqrt(liczba);i++){
        if(liczba%i==0)
            return false;
    }
    return true;
}

int rozklad(int liczba){
    int wynik=0;
    int dzielnik=2;
    while(liczba>1){
        if(czy_pierwsza(dzielnik)){
            while(liczba%dzielnik==0){
                wynik=wynik+dzielnik;
                liczba=liczba/dzielnik;
            }
        }
        dzielnik++;
    }
    return wynik;
}

void podzadanie1(){
    ifstream plik("kebab.txt");
    int a;
    int maks=0;
    int pom=0;
    int pom2=0;
    int ile=0;
    vector <int> maksymalne;
    while(!plik.eof()){
        plik>>a;
        pom2=a;
        while(pom!=rozklad(pom2)){
            ile++;
            pom2=pom;
            pom=rozklad(pom2);
        }
        if(ile>=maks){
            if(ile==maks)
                maksymalne.push_back(a);
            else{
                maksymalne.clear();
                maks=ile;
                maksymalne.push_back(a);
            }
        }
        ile=0;
    }
    cout<<ile;
    for(int i=0;i<maksymalne.size();i++){
        cout<<maksymalne[i]<<endl;
    }
}

int main(){
    podzadanie1();
}
