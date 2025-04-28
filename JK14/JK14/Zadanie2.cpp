#include <bits/stdc++.h>
using namespace std;

int system(string liczba){
    int minimalny=2;
    int maksymalny=16;
    int pom=0;
    for(int i=0;i<liczba.size();i++){
        if(liczba[i]=='0'||liczba[i]=='1')
            pom=2;
        if(liczba[i]=='2')
            pom=3;
        if(liczba[i]=='3')
            pom=4;
        if(liczba[i]=='4')
            pom=5;
        if(liczba[i]=='5')
            pom=6;
        if(liczba[i]=='6')
            pom=7;
        if(liczba[i]=='7')
            pom=8;
        if(liczba[i]=='8')
            pom=9;
        if(liczba[i]=='9')
            pom=10;
        if(liczba[i]=='A')
            pom=11;
        if(liczba[i]=='B')
            pom=12;
        if(liczba[i]=='C')
            pom=13;
        if(liczba[i]=='D')
            pom=14;
        if(liczba[i]=='E')
            pom=15;
        if(liczba[i]=='F')
            pom=16;
        if(pom>minimalny)
            minimalny=pom;
    }
    return minimalny;
}

void podzadanie1(){
    ifstream plik("liczby.txt");
    string a;
    string b;
    int Tab[15];
    int syst;
    for(int i=0;i<15;i++){
        Tab[i]=0;
    }
    while(!plik.eof()){
        plik>>a>>b;
        syst=max(system(a),system(b));
        Tab[syst-2]=Tab[syst-2]+1;
    }
    for(int i=0;i<15;i++){
        cout<<i+2<<": "<<Tab[i]<<endl;
    }
}

int przeliczanie(string liczba, int system){
    int wynik=0;
    for(int i=0;i<liczba.size();i++){
        if(liczba[i]=='A'){
            wynik=wynik+10*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='B'){
            wynik=wynik+11*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='C'){
            wynik=wynik+12*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='D'){
            wynik=wynik+13*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='E'){
            wynik=wynik+14*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='F'){
            wynik=wynik+15*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='0'){
            wynik=wynik+0*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='1'){
            wynik=wynik+1*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='2'){
            wynik=wynik+2*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='3'){
            wynik=wynik+3*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='4'){
            wynik=wynik+4*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='5'){
            wynik=wynik+5*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='6'){
            wynik=wynik+6*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='7'){
            wynik=wynik+7*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='8'){
            wynik=wynik+8*pow(system,liczba.size()-1-i);
        }
        if(liczba[i]=='9'){
            wynik=wynik+9*pow(system,liczba.size()-1-i);
        }
    }
    return wynik;
}

void podzadanie2(){
    string a;
    string b;
    int syst;
    int mini=INT_MAX;
    int maks=0;
    int pom=0;
    int pom2=0;
    string najwieksza;
    string najmniejsza;
    ifstream plik("liczby.txt");
    while(!plik.eof()){
        plik>>a>>b;
        syst=max(system(a),system(b));
        pom=przeliczanie(a,syst);
        pom2=przeliczanie(b,syst);
        if(pom>maks){
            maks=pom;
            najwieksza=a;
        }
        if(pom2>maks){
            maks=pom2;
            najwieksza=b;
        }
        if(pom<mini){
            mini=pom;
            najmniejsza=a;
        }
        if(pom2<mini){
            mini=pom2;
            najmniejsza=b;
        }
    }
    cout<<najmniejsza<<" "<<najwieksza;
}

int main(){
    //podzadanie1();
    podzadanie2();
}
