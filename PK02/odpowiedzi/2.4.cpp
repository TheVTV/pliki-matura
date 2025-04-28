#include <iostream>
#include <fstream>
#include <map>
#include <string>
using namespace std;

int sys(string napis)
{
    char champ=napis[0];
    for(int i=1;i<napis.length();i++)
    {
        if(champ<=napis[i])
        {
            champ=napis[i];
        }
    }
    if(champ>='A')
    {
        return int(champ-'A')+11;
    }
    return int(champ-'0')+1;
}

int main()
{
    pair<string,string> liczby;
    fstream plik;
    plik.open("liczby.txt",ios::in);
    map<int,int> systemy;
    int counter=0;
    while(plik.good())
    {
        plik>>liczby.first;
        plik>>liczby.second;
        systemy[sys(liczby.second)]++;
        counter++;
    }
    for(int i=2;i<17;i++)
    {
        string s=to_string(double(systemy[i])/counter*100);

        cout<<i<<": ";
        for(int i=0;i<4;i++)
        {
            cout<<s[i];
        }
        cout<<endl;
    }
    return 0;
}
