#include <iostream>
#include <fstream>
#include <map>
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
    while(plik.good())
    {
        plik>>liczby.first;
        plik>>liczby.second;
        systemy[sys(liczby.second)]++;
    }
    for(int i=2;i<17;i++)
    {
        cout<<i<<": "<<systemy[i]<<endl;
    }
    ///co to znaczy ¿e liczby s¹ w tym samym systemie liczbowym, ale druga jest pierwsz¹ w odwrotnej kolejnoœci w systemie 10tnym?
    //jeœli jest system 16stkowy, to odwrotna kolejnoœæ bêdzie 11FF-FF11 jeœli s¹ w tym samym systemie huh?
    return 0;
}
