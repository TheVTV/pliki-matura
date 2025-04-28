#include <iostream>
#include <fstream>
#include <map>
using namespace std;
int f(string k)
{
    char maxs;
    maxs=k[0];
    for (int i=1;i<k.length();i++) {
        if (k[i]>maxs) {
            maxs=k[i];
        }
    }
    if(maxs>='A') {
        return maxs-'A';
    }
    else {
        return maxs-'0';
    }
}
int main()
{
    fstream plik;
    plik.open("liczby.txt",ios::in);
    pair<string,string> liczby;
    map<int,int> ile;
    int sys;
    while ((plik.good())) {
        plik>>liczby.first>>liczby.second;
        if(f(liczby.first)==f(liczby.second)) {
            ile[f(liczby.first)]++;
        }
    }
    for (int i=0;i<16;i++) {
        cout<<i+2<<": "<<ile[i]<<endl;
    }
    return 0;
}