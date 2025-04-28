#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;
//codeblocksowe skill issue z mojej strony
pair<int,int> f(int a) {
    vector<int> v,v2;
    int counter=0,kebab=0,i=2,ends=0,starts=a;
    while (starts!=ends) {
        counter++;
        starts=ends;
        ends=0;
        while (starts>1) {
            if (starts%i==0) {
                starts/=i;
                v.push_back(i);
            }
            else {
                i++;
            }
        }
        i=2;
        for (const auto &it : v) {
            ends+=it;
        }
        v2.push_back(ends);
        v.clear();
    }
    for (const auto &it : v2) {
        kebab+=it;
    }
    return {starts,counter};
}
int main()
{
    fstream plik;
    plik.open("kebab_przyklad.txt",ios::in);
    int liczba;
    int champ=0;
    vector<int> champs;
    while (plik.good()) {
        plik>>liczba;
        if (f(liczba).second>champ) {
            champ=f(liczba).second;
            champs.push_back(liczba);
        }
    }
    cout<<champ;
    for (const auto &it : champs) {
        cout<<it<<"\n";
    }
    return 0;
}